from google.protobuf.empty_pb2 import Empty

from ..rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from ..rpc.gen.rustic_poker_pb2 import GetLobbiesResponse
from .utils import call


def list_lobbies_rpc(stub: RusticPokerStub) -> GetLobbiesResponse:
    """
    Lists available game lobbies.
    """

    req = Empty()
    res: GetLobbiesResponse = call(stub.GetLobbies, req)
    return res
