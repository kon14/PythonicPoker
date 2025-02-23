from typing import Callable
from pygame import Surface

from .types import View
from ..connection import ServerConnection
from ..player import PlayerIdentity


from pythonic_poker_sdk import list_lobbies_rpc, RusticPokerStub

def game_logic(
    view: View,
    set_view: Callable[[View], None],
    canvas: Surface,
    connection: ServerConnection,
    player: PlayerIdentity,
):
    pass

    lobbies = list_lobbies_rpc(connection.stub)
    print(lobbies)
