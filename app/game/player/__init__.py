import os


PEER_ADDRESS_ENV = "PEER_ADDRESS"
DEFAULT_PEER_ADDRESS = "192.124.234.25"


def get_peer_address() -> str:
    peer_address = os.getenv(PEER_ADDRESS_ENV)
    while peer_address is None or len(peer_address) == 0:
        print(f"Specify desired player peer address: (default: {DEFAULT_PEER_ADDRESS})")
        peer_address = input("> ").strip() or DEFAULT_PEER_ADDRESS
    return peer_address
