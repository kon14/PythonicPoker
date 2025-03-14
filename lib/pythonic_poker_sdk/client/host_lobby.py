from ..rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from ..rpc.gen.rustic_poker_pb2 import CreateLobbyRequest, LobbyInfoPublic
from ..types import PlayerIdentity
from .utils import call_with_metadata


def host_lobby_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
    lobby_name: str,
):
    """
    Creates a new game lobby.\n
    Player automatically joins the lobby.
    """

    req = CreateLobbyRequest(
        lobby_name=lobby_name,
    )
    res: LobbyInfoPublic = call_with_metadata(
        player.peer_address,
        stub.CreateLobby,
        req,
    )
    return res
