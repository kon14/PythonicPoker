
def call_with_metadata(
    peer_address: str,
    method,
    request,
):
    metadata = [("peer-address", peer_address)]
    return method(request=request, metadata=metadata)
