from google.protobuf.empty_pb2 import Empty

from .gen.rustic_poker_pb2_grpc import RusticPokerStub


def list_lobbies_rpc(stub: RusticPokerStub):
    """
    Lists available game lobbies.
    """

    req = Empty()
    res = stub.GetLobbies(req)
    return res
