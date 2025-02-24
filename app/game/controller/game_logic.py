import pygame
from typing import Callable, List

from pythonic_poker_sdk import RusticPokerStub, PlayerIdentity, list_lobbies_rpc, connect_rpc

from app.game import views
from .types import View
from ..connection import ServerConnection, get_server_connection
from ..player import get_peer_address


def game_logic(
    view: View,
    set_view: Callable[[View], None],
    set_connection: Callable[[ServerConnection], None],
    set_player: Callable[[PlayerIdentity], None],
    canvas: pygame.Surface,
    connection: ServerConnection | None,
    player: PlayerIdentity | None,
    events: List[pygame.event.Event],
):
    if view == "server-selection":
        connection = get_server_connection() # TODO: GUI-aware handler
        set_connection(connection)
        set_view("player-login")

    elif view == "player-login":
        assert connection is not None
        peer_address = get_peer_address()
        player = PlayerIdentity(peer_address) # TODO: GUI-aware handler
        connect_rpc(connection.stub, player)
        set_player(player)
        set_view("lobby-selection")

    elif view == "lobby-selection":
        assert connection is not None
        assert player is not None
        on_lobby_join = lambda: set_view("lobby")
        on_lobby_create = lambda: set_view("lobby-creation")
        data = views.lobby.selection.act(
            conn=connection,
            player=player,
            on_lobby_join=on_lobby_join,
            on_lobby_create=on_lobby_create,
        )
        views.lobby.selection.handle_events(events)
        views.lobby.selection.render(data, canvas)

    # elif view == "lobby-creation":
    #     assert connection is not None
    #     assert player is not None
    #     on_lobby_create = lambda: set_view("lobby")
    #     on_cancel = lambda: set_view("lobby-selection")
    #     data = views.lobby.creation.act(
    #         conn=connection,
    #         on_lobby_create=on_lobby_create,
    #         on_cancel=on_cancel,
    #     )
    #     # TODO: pass in lobby selection state setter, view setting closure
    #     views.lobby.creation.render(data, canvas)

    elif view == "lobby":
        assert connection is not None
        assert player is not None
        pass

    elif view == "poker-ante":
        assert connection is not None
        assert player is not None
        pass

    elif view == "poker-dealing":
        assert connection is not None
        assert player is not None
        pass

    elif view == "poker-betting":
        assert connection is not None
        assert player is not None
        pass

    elif view == "poker-drawing":
        assert connection is not None
        assert player is not None
        pass

    elif view == "poker-showdown":
        assert connection is not None
        assert player is not None
        pass

    else:
        print("Invalid view specified!")
