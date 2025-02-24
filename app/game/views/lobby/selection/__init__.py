import pygame
from typing import Collection, Callable, List, Tuple, Dict

from pythonic_poker_sdk import RusticPokerStub, LobbyInfoPublic, LobbyStatus, list_lobbies_rpc, join_lobby_rpc, PlayerIdentity
from app.game.connection import ServerConnection
from app.constants import CANVAS_RESOLUTION
from app.constants.color import *

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
    col_widths = [300, 300, 400, 350]
    font = pygame.font.SysFont("Arial", 20)
    canvas.fill(WHITE_COLOR)

    # Draw Table Header
    y_offset = 50
    for col, header in enumerate(headers):
        header_text = font.render(header, True, BLACK_COLOR)
        canvas.blit(header_text, (col * col_widths[col] + CELL_PADDING, y_offset))

    # Draw Separator
    pygame.draw.line(canvas, BLACK_COLOR, (0, y_offset + 30), (CANVAS_RESOLUTION[0], y_offset + 30), 2)

    # Draw Table Rows
    y_offset += 40
    for lobby in lobbies:
        text_col_y_offset = 5
        # TODO: host_player_id -> host_player_name
        for col, key in enumerate(["name", "host_player_id", "player_count", "status"]):
            value = getattr(lobby, key)
            if key == "status":
                value = LobbyStatus.Name(value)
            cell_text = font.render(str(value), True, BLACK_COLOR)
            canvas.blit(cell_text, (col * col_widths[col] + CELL_PADDING, y_offset + text_col_y_offset))

        # TODO: only show btn for join-able lobbies
        join_btn_handler = lambda : join_lobby(lobby.lobby_id)
        join_btn_surf = Button.build_surf("Join", BLACK_COLOR, JOIN_COLOR, 20, 5)
        join_btn = Button(
            id=lobby.lobby_id,
            surf=join_btn_surf,
            pos=(col * col_widths[col] + CELL_PADDING, y_offset),
            handler=join_btn_handler,
        )
        join_btn.register_event_handler(event_handlers) # TODO: cleanup dead lobbies...
        join_btn.draw(canvas)
        y_offset += 50

    pygame.draw.rect(canvas, BLACK_COLOR, pygame.Rect(0, 50, CANVAS_RESOLUTION[0], y_offset - 50), 2)


class Button:
    def __init__(
        self,
        id: str,
        surf: pygame.Surface,
        pos: Tuple[int, int],
        handler: Callable[[], None],
    ):
        self.id = id
        self.surf = surf
        self.rect = surf.get_rect()
        self.rect.topleft = pos
        self.handler = handler


    def draw(self, canvas):
        canvas.blit(self.surf, self.rect)


    def register_event_handler(
        self,
        event_handlers: Dict[str, Callable[[pygame.event.Event], None]],
    ):
        event_handlers[self.id] = self.__check_click


    def __check_click(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("ev pos: ", event.pos, " self pos: ", self.rect)
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            print("AHHHHHHH")
            self.handler()


    @staticmethod
    def build_surf(
        text: str,
        txt_color: Tuple[int, int, int],
        bg_color: Tuple[int, int, int],
        font_size: int,
        padding: int = 0,
    ):
        font = pygame.font.SysFont("Arial", font_size)
        text_surface = font.render(text, True, txt_color)
        text_width, text_height = text_surface.get_size()
        bg_width = text_width + 2 * padding
        bg_height = text_height + 2 * padding
        bg_surface = pygame.Surface((bg_width, bg_height))
        bg_surface.fill(bg_color)
        text_rect = text_surface.get_rect(center=(bg_width // 2, bg_height // 2))
        bg_surface.blit(text_surface, text_rect)
        return bg_surface
