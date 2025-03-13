import pygame
from typing import Callable, List, Optional

from pythonic_poker_sdk import PlayerIdentity, connect_rpc, GameState

from app.game import views
from ..views.types import View
from ..connection import ServerConnection, get_server_connection
from ..player import get_peer_address
from ..events import PythonicPokerEvent


def game_logic(
    view: View,
    set_connection: Callable[[ServerConnection], None],
    set_player: Callable[[PlayerIdentity], None],
    canvas: pygame.Surface,
    connection: Optional[ServerConnection],
    player: Optional[PlayerIdentity],
    game_state: Optional[GameState],
    events: List[pygame.event.Event],
):
    if view == "server-selection":
        connection = get_server_connection() # TODO: GUI-aware handler
        set_connection(connection)
        PythonicPokerEvent.set_view("player-login")

    elif view == "player-login":
        assert connection is not None
        peer_address = get_peer_address()
        player = PlayerIdentity(peer_address) # TODO: GUI-aware handler
        connect_rpc(connection.stub, player)
        set_player(player)
        PythonicPokerEvent.set_view("lobby-selection")
        # TODO: Application Crash Recovery
        # check player in-game status
        # if in-game: send START_LOBBY_MATCH event (proc watch stream)

    elif view == "lobby-selection":
        assert connection is not None
        assert player is not None
        data = views.lobby.selection.act(conn=connection)
        views.lobby.selection.render(data, canvas)
        views.lobby.selection.handle_events(events)

    elif view == "lobby-creation":
        assert connection is not None
        assert player is not None
        data = views.lobby.host.act()
        views.lobby.host.render(data, canvas)
        views.lobby.host.handle_events(events)

    elif view == "lobby":
        assert connection is not None
        assert player is not None
        if game_state is None:
            # Waiting for WatchState stream
            return
        assert game_state is not None
        data = views.lobby.inner.act(game_state)
        views.lobby.inner.render(data, canvas)
        views.lobby.inner.handle_events(events)

    elif view == "poker-ante":
        assert connection is not None
        assert player is not None
        # TODO
        views.game.ante.render(canvas, game_state)

    elif view == "poker-dealing":
        assert connection is not None
        assert player is not None
        # TODO
        views.game.dealing.render(canvas, game_state)

    elif view.startswith("poker-betting"):
        assert connection is not None
        assert player is not None
        views.game.betting.render(canvas, game_state)
        if view == "poker-betting":
            views.game.phases.betting.handle_events(events)
        elif view == "poker-betting-bet-modal":
            views.game.betting.bet_modal.render(canvas, game_state)
            views.game.phases.betting.bet_modal.handle_events(events)

    elif view == "poker-drawing":
        assert connection is not None
        assert player is not None
        # TODO
        views.game.drawing.render(canvas, game_state)

    elif view == "poker-showdown":
        assert connection is not None
        assert player is not None
        # TODO
        views.game.showdown.render(canvas, game_state)

    else:
        print("Invalid view specified!")
