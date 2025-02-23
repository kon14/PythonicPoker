from google.protobuf.empty_pb2 import Empty

from app.game.player import PlayerIdentity
from ..grpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from ..grpc.gen.rustic_poker_pb2 import SetLobbyMatchmakingStatusRequest
from .utils import call_with_metadata


def set_lobby_matchmaking_status_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
    matchmaking: bool,
):
    """
    Sets lobby matchmaking status.\n
    Only callable by lobby host!\n
    Host player automatically accepts matchmaking.
    """

    req = SetLobbyMatchmakingStatusRequest(
        status=
            SetLobbyMatchmakingStatusRequest.MATCHMAKING if matchmaking
            else SetLobbyMatchmakingStatusRequest.NOT_MATCHMAKING
    )
    _: Empty = call_with_metadata(
        player.peer_address,
        stub.SetLobbyMatchmakingStatus,
        req,
    )
