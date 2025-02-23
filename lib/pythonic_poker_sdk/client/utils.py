from google.protobuf.json_format import MessageToDict, ParseDict


def call_with_metadata(
    peer_address: str,
    method,
    request,
):
    metadata = [("peer-address", peer_address)]
    response = method(request=request, metadata=metadata)
    return preserve_omitted_fields(response)


def call(
    method,
    request,
):
    response = method(request=request)
    return preserve_omitted_fields(response)


def preserve_omitted_fields(grpc_response):
    """
    gRPC and Protobuf 3 omit fields with default values to reduce message size.\n
    However, Python's generated gRPC client code doesn't handle this, causing
    missing fields to be treated as absent.\n
    This function ensures that omitted fields' default values are re-introduced,
    ensuring the response matches the expected schema and preventing issues with missing data.
    """

    if hasattr(grpc_response, "__iter__"):
        return (ensure_defaults(message) for message in grpc_response)
    else:
        return ensure_defaults(grpc_response)


def ensure_defaults(proto_message):
    message_dict = MessageToDict(proto_message, always_print_fields_with_no_presence=True)

    for field in proto_message.DESCRIPTOR.fields:
        field_name = field.name
        if field.label != field.LABEL_REPEATED and field.name not in message_dict:
            if field.cpp_type == field.CPPTYPE_MESSAGE:
                message_dict[field_name] = ParseDict({}, field.message_type)
            else:
                message_dict[field_name] = field.default_value

    updated_message = ParseDict(message_dict, proto_message.__class__())

    return updated_message
