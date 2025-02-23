from google.protobuf.empty_pb2 import Empty

from ..rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from ..rpc.gen.rustic_poker_pb2 import ConnectRequest
from ..types import PlayerIdentity
from .utils import call_with_metadata


def connect_rpc(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    """
    Initiates a game server connection for the player.\n
    No other actions may take place before this one!
    """

    req = ConnectRequest(
        # player_name=player.name,
    )
    _: Empty = call_with_metadata(
        player.peer_address,
        stub.Connect,
        req,
    )
