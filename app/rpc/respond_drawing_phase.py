from typing import List
from google.protobuf.empty_pb2 import Empty

from app.game.player import PlayerIdentity
from .gen.rustic_poker_pb2_grpc import RusticPokerStub
from .gen.rustic_poker_pb2 import RespondDrawingPhaseRequest, Card
from .utils import call_with_metadata


def respond_drawing_phase_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
    discarded_cards: List[Card] | None
):
    """
    Takes a drawing phase action.
    """

    req = RespondDrawingPhaseRequest()
    _: Empty = call_with_metadata(
        player.peer_address,
        stub.RespondDrawingPhase,
        req,
    )
