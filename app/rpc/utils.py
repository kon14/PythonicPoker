from google.protobuf.json_format import MessageToJson


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
    This function ensures that omitted fields are re-added with their default values,
    ensuring the response matches the expected schema and preventing issues with missing data.
    """

    if hasattr(grpc_response, "__iter__"):
        return (MessageToJson(
            message,
            always_print_fields_with_no_presence=True
        ) for message in grpc_response)
    else:
        return MessageToJson(
            grpc_response,
            always_print_fields_with_no_presence=True
        )
