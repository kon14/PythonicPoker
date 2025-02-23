from google.protobuf.empty_pb2 import Empty

from ..rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from ..rpc.gen.rustic_poker_pb2 import RespondLobbyMatchmakingRequest
from ..types import PlayerIdentity
from .utils import call_with_metadata


def respond_lobby_matchmaking_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
    accept: bool,
):
    """
    Sets lobby matchmaking acceptance for player.
    """

    req = RespondLobbyMatchmakingRequest(
        decision=
            RespondLobbyMatchmakingRequest.MatchmakingDecision.ACCEPT if accept
            else RespondLobbyMatchmakingRequest.MatchmakingDecision.DECLINE
    )
    _: Empty = call_with_metadata(
        player.peer_address,
        stub.RespondLobbyMatchmaking,
        req,
    )
