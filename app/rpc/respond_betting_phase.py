from google.protobuf.empty_pb2 import Empty

from app.game.player import PlayerIdentity
from .gen.rustic_poker_pb2_grpc import RusticPokerStub
# from .gen.rustic_poker_pb2 import RespondBettingPhaseRequest
from .utils import call_with_metadata


def respond_betting_phase_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
    req #: RespondBettingPhaseRequest.MatchmakingDecision,
):
    """
    Takes a betting phase action.
    """

    _: Empty = call_with_metadata(
        player.peer_address,
        stub.RespondBettingPhase,
        req,
    )
