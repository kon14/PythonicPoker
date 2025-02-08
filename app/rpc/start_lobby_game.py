from google.protobuf.empty_pb2 import Empty

from app.game.player import PlayerIdentity
from .gen.rustic_poker_pb2_grpc import RusticPokerStub
from .utils import call_with_metadata


def start_lobby_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    """
    Starts a Poker game.\n
    Lobby must be in matchmaking status with all players having accepted matchmaking.
    """

    req = Empty()
    _: Empty = call_with_metadata(
        player.peer_address,
        stub.StartLobbyGame,
        req,
    )
