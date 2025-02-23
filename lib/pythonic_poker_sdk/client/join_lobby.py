from ..rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from ..rpc.gen.rustic_poker_pb2 import JoinLobbyRequest
from ..types import PlayerIdentity
from .utils import call_with_metadata


def join_lobby_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
    lobby_id: str,
):
    """
    Joins a game lobby.
    """

    req = JoinLobbyRequest(
        lobby_id=lobby_id,
    )
    res = call_with_metadata(
        player.peer_address,
        stub.JoinLobby,
        req,
    )
    return res
