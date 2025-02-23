from google.protobuf.empty_pb2 import Empty

from ..rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from ..types import PlayerIdentity
from .utils import call_with_metadata


def leave_lobby_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    """
    Leaves the previously joined lobby.
    """
    req = Empty()
    _: Empty = call_with_metadata(
        player.peer_address,
        stub.LeaveLobby,
        req,
    )
