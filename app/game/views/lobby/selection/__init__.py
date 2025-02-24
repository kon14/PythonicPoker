import pygame
from typing import Collection, Callable, List, Tuple

from pythonic_poker_sdk import RusticPokerStub, LobbyInfoPublic, LobbyStatus, list_lobbies_rpc, join_lobby_rpc, PlayerIdentity
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
TABLE_COLOR = (200, 200, 200)
JOIN_COLOR = (255, 100, 0)
HEADER_COLOR = (100, 100, 255)
CELL_PADDING = 10


def act(
    conn: ServerConnection,
    player: PlayerIdentity,
    on_lobby_join: Callable[[], None],
    on_lobby_create: Callable[[], None],
):
    lobbies_res = __poll_data(conn)
    join_lobby = lambda lobby_id : __join_lobby(conn, player, lobby_id, on_lobby_join)
    create_lobby = lambda : on_lobby_create()
    return (lobbies_res.lobbies, join_lobby, create_lobby)


def render(data, canvas: pygame.Surface):
    lobbies = data[0]
    join_lobby = data[1]
    create_lobby = data[2]
    __draw_table(canvas, lobbies, join_lobby, create_lobby)


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
    on_lobby_join: Callable[[], None],
):
    try:
        join_lobby_rpc(conn.stub, player, lobby_id)
    except Exception as err:
        print(f"Failed to join lobby ({lobby_id})!")
        print(err)
        return
    on_lobby_join()


def __draw_table(
    canvas: pygame.Surface,
    lobbies: Collection[LobbyInfoPublic],
    join_lobby: Callable[[str], None],
    create_lobby: Callable[[], None],
):
    global event_handlers
    headers = ["Lobby Name", "Host Player", "Player Count", "Lobby Status"]
    col_widths = [400, 400, 150, 200, 200]
    font = pygame.font.SysFont("Arial", 20)
    canvas.fill(WHITE_COLOR)

    # Draw Table Header
    y_offset = 50

    # Draw Header
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
                __draw_join_btn(canvas, lobby.lobby_id, join_lobby, (x_offset, y_offset))
            else:
                value = getattr(lobby, key)
                if isinstance(value, str):
                    value = truncate_text(getattr(lobby, key), 25)
                if key == "status":
                    value = LobbyStatus.Name(value)
                cell_text = font.render(str(value), True, BLACK_COLOR)
                canvas.blit(cell_text, (x_offset, y_offset + text_col_y_offset))
        y_offset += 50

    pygame.draw.rect(canvas, BLACK_COLOR, pygame.Rect(0, 50, CANVAS_RESOLUTION[0], y_offset - 50), 2)


def __draw_join_btn(
    canvas: pygame.Surface,
    lobby_id: str,
    join_lobby: Callable[[str], None],
    pos: Tuple[int, int],
):
    join_btn_handler = lambda: join_lobby(lobby_id)
    join_btn_surf = Button.build_surf("Join", BLACK_COLOR, JOIN_COLOR, 20, 5)
    join_btn = Button(
        id=lobby_id,
        surf=join_btn_surf,
        pos=pos,
        handler=join_btn_handler,
    )
    join_btn.register_event_handler(event_handlers)  # TODO: cleanup dead lobbies...
    join_btn.draw(canvas)
