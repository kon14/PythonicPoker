from google.protobuf.empty_pb2 import Empty

from ..rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
# from ..grpc.gen.rustic_poker_pb2 import RespondBettingPhaseRequest
from ..types import PlayerIdentity
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
