from google.protobuf.empty_pb2 import Empty
from typing import Iterator

from app.game.player import PlayerIdentity
from ..grpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from ..grpc.gen.rustic_poker_pb2 import GameState
from .utils import call_with_metadata


def watch_state_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    """
    Initiates a server-side stream of game state updates.\n
    Player must be participating in a lobby!
    """

    req = Empty()
    game_state_stream: Iterator[GameState] = call_with_metadata(
        player.peer_address,
        stub.WatchState,
        req,
    )

    for state in game_state_stream:
        # This is only writing to stdout as a demonstration...
        print(state)
        pass
