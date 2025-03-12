import pygame
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer
from typing import Collection, Callable, List, Tuple, NamedTuple

from pythonic_poker_sdk import LobbyInfoPublic, LobbyStatus, list_lobbies_rpc
from app.game.events import PythonicPokerEvent
from app.game.connection import ServerConnection
from app.components import Button
from app.constants import CANVAS_RESOLUTION
from app.constants.color import *
from app.utils import truncate_text, deep_getattr


# Data
POLL_INTERVAL_MS = 500
last_call_time = 0
last_lobbies_res = None
event_handlers = {}

# Rendering
CELL_PADDING = 10
BACKGROUND_COLOR = (20, 20, 20)


class LobbySelectionViewRenderArgs(NamedTuple):
    lobbies: RepeatedCompositeFieldContainer[LobbyInfoPublic]
    host_lobby_handler: Callable[[], None]
    join_lobby_handler: Callable[[str], None]


def act(conn: ServerConnection):
    lobbies_res = __poll_data(conn)

    host_lobby_handler = lambda : PythonicPokerEvent.set_view("lobby-creation")
    join_lobby_handler = lambda lobby_id : PythonicPokerEvent.join_lobby(lobby_id)

    return LobbySelectionViewRenderArgs(
        lobbies_res.lobbies,
        host_lobby_handler,
        join_lobby_handler,
    )


def render(args: LobbySelectionViewRenderArgs, canvas: pygame.Surface):
    __draw_table(
        canvas,
        args.lobbies,
        args.join_lobby_handler,
        args.host_lobby_handler,
    )


def handle_events(events: List[pygame.event.Event]):
    global event_handlers
    for event in events:
        for handler in event_handlers.values():
            handler(event)


def __poll_data(conn: ServerConnection):
    global last_call_time, last_lobbies_res
    current_time = pygame.time.get_ticks()
    if last_lobbies_res is None or current_time - last_call_time >= POLL_INTERVAL_MS:
        last_lobbies_res = list_lobbies_rpc(conn.stub)
        last_call_time = current_time
    return last_lobbies_res


def __draw_table(
    canvas: pygame.Surface,
    lobbies: Collection[LobbyInfoPublic],
    join_lobby_handler: Callable[[str], None],
    host_lobby_handler: Callable[[], None],
):
    global event_handlers
    headers = ["Lobby Name", "Host Player", "Min Players", "Max Players", "Player Count", "Lobby Status"]
    col_widths = [300, 230, 150, 150, 150, 150, 200]
    font = pygame.font.SysFont("Arial", 20)
    canvas.fill(BACKGROUND_COLOR)

    starting_y_offset = 60
    y_offset = starting_y_offset

    # Draw Host Lobby Button
    __draw_host_btn(canvas, host_lobby_handler, (1140, 10))

    # Draw Table Header
    y_offset += 5
    for col, header in enumerate(headers):
        header_text = font.render(header, True, WHITE_COLOR)
        x_offset = sum(col_widths[:col]) + (CELL_PADDING * (col + 1))
        canvas.blit(header_text, (x_offset, y_offset))

    # Draw Separator
    y_offset += 25
    pygame.draw.line(canvas, WHITE_COLOR, (0, y_offset), (CANVAS_RESOLUTION[0], y_offset), 2)

    # Draw Table Rows
    for lobby in lobbies:
        y_offset += 15
        for col, key in enumerate(["name", "host_player.player_name", "settings.min_players", "settings.max_players", "player_count", "status", ""]):
            x_offset = sum(col_widths[:col]) + (CELL_PADDING * (col + 1))
            if key == "":
                # Join Button
                __draw_join_btn(
                    canvas,
                    lobby.lobby_id,
                    lobby.is_joinable,
                    join_lobby_handler,
                    (x_offset, y_offset),
                )
            else:
                value = deep_getattr(lobby, key)
                if isinstance(value, str):
                    value = truncate_text(value, 25)
                if key == "status":
                    value = LobbyStatus.Name(value)
                cell_text = font.render(str(value), True, WHITE_COLOR)
                canvas.blit(cell_text, (x_offset, y_offset))
        y_offset += 40

    pygame.draw.rect(canvas, WHITE_COLOR, pygame.Rect(0, starting_y_offset, CANVAS_RESOLUTION[0], y_offset - 50), 2)


def __draw_host_btn(
    canvas: pygame.Surface,
    host_lobby_handler: Callable[[], None],
    pos: Tuple[int, int],
):
    btn = Button(
        id="btn-lobby-host",
        text="Host Lobby",
        pos=pos,
        event_handlers=event_handlers,
        handler=host_lobby_handler,
    )
    btn.draw(canvas)


def __draw_join_btn(
    canvas: pygame.Surface,
    lobby_id: str,
    is_joinable: bool,
    join_lobby_handler: Callable[[str], None],
    pos: Tuple[int, int],
):
    btn = Button(
        id=f"btn-lobby-join-{lobby_id}",
        text="Join",
        pos=pos,
        event_handlers=event_handlers,
        handler=lambda: join_lobby_handler(lobby_id),
    )
    if is_joinable:
        btn.enable()
    else:
        btn.disable()
    btn.draw(canvas)
