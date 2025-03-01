import pygame
from typing import Collection, Callable, List, Tuple

from pythonic_poker_sdk import LobbyInfoPublic, LobbyStatus, list_lobbies_rpc, join_lobby_rpc, PlayerIdentity
from app.game.connection import ServerConnection
from app.components import Button
from app.constants import CANVAS_RESOLUTION
from app.constants.color import *
from app.utils import truncate_text


# Data
POLL_INTERVAL_MS = 500
last_call_time = 0
last_lobbies_res = None
event_handlers = {}

# Rendering
CELL_PADDING = 10


def act(
    conn: ServerConnection,
    player: PlayerIdentity,
    on_lobby_join: Callable[[str], None],
    on_lobby_host: Callable[[], None],
):
    lobbies_res = __poll_data(conn)
    join_lobby = lambda lobby_id : __join_lobby(conn, player, lobby_id, on_lobby_join)
    host_lobby = lambda : on_lobby_host()
    return (lobbies_res.lobbies, join_lobby, host_lobby)


def render(data, canvas: pygame.Surface):
    lobbies = data[0]
    join_lobby = data[1]
    host_lobby = data[2]
    __draw_table(canvas, lobbies, join_lobby, host_lobby)


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


def __join_lobby(
    conn: ServerConnection,
    player: PlayerIdentity,
    lobby_id: str,
    on_lobby_join: Callable[[str], None],
):
    try:
        join_lobby_rpc(conn.stub, player, lobby_id)
    except Exception as err:
        print(f"Failed to join lobby ({lobby_id})!")
        print(err)
        return
    on_lobby_join(lobby_id)


def __draw_table(
    canvas: pygame.Surface,
    lobbies: Collection[LobbyInfoPublic],
    join_lobby: Callable[[str], None],
    host_lobby: Callable[[], None],
):
    global event_handlers
    headers = ["Lobby Name", "Host Player", "Player Count", "Lobby Status"]
    col_widths = [400, 400, 150, 200, 200]
    font = pygame.font.SysFont("Arial", 20)
    canvas.fill(WHITE_COLOR)

    starting_y_offset = 60
    y_offset = starting_y_offset

    # Draw Host Lobby Button
    __draw_host_btn(canvas, host_lobby, (1140, 10))

    # Draw Table Header
    for col, header in enumerate(headers):
        header_text = font.render(header, True, BLACK_COLOR)
        x_offset = sum(col_widths[:col]) + (CELL_PADDING * (col + 1))
        canvas.blit(header_text, (x_offset, y_offset))

    # Draw Separator
    pygame.draw.line(canvas, BLACK_COLOR, (0, y_offset + 30), (CANVAS_RESOLUTION[0], y_offset + 30), 2)

    # Draw Table Rows
    y_offset += 40
    for lobby in lobbies:
        text_col_y_offset = 5
        # TODO: host_player_id -> host_player_name
        for col, key in enumerate(["name", "host_player_id", "player_count", "status", ""]):
            x_offset = sum(col_widths[:col]) + (CELL_PADDING * (col + 1))
            if key == "":
                # Join Button
                # TODO: only show btn for join-able lobbies
                join_lobby_handler = lambda: join_lobby(lobby.lobby_id)
                __draw_join_btn(canvas, lobby.lobby_id, join_lobby_handler, (x_offset, y_offset))
            else:
                value = getattr(lobby, key)
                if isinstance(value, str):
                    value = truncate_text(getattr(lobby, key), 25)
                if key == "status":
                    value = LobbyStatus.Name(value)
                cell_text = font.render(str(value), True, BLACK_COLOR)
                canvas.blit(cell_text, (x_offset, y_offset + text_col_y_offset))
        y_offset += 50

    pygame.draw.rect(canvas, BLACK_COLOR, pygame.Rect(0, starting_y_offset, CANVAS_RESOLUTION[0], y_offset - 50), 2)


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
    join_lobby_handler: Callable[[], None],
    pos: Tuple[int, int],
):
    btn = Button(
        id=f"btn-lobby-join-{lobby_id}",
        text="Join",
        pos=pos,
        event_handlers=event_handlers,
        handler=join_lobby_handler,
    )
    btn.draw(canvas)
