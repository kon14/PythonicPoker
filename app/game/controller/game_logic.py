from typing import Callable
from pygame import Surface

from pythonic_poker_sdk import RusticPokerStub, PlayerIdentity, list_lobbies_rpc
from .types import View
from ..connection import ServerConnection


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
