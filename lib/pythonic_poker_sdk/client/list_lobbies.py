from google.protobuf.empty_pb2 import Empty

from ..grpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from .utils import call


def list_lobbies_rpc(stub: RusticPokerStub):
    """
    Lists available game lobbies.
    """

    req = Empty()
    res = call(stub.GetLobbies, req)
    return res
