from typing import Collection
import pygame

from pythonic_poker_sdk import RusticPokerStub, LobbyInfoPublic, LobbyStatus, list_lobbies_rpc
from app.game.connection import ServerConnection
from app.constants import CANVAS_RESOLUTION
from app.constants.color import *

# Data
POLL_INTERVAL_MS = 500
last_call_time = 0
last_lobbies_res = None

# Rendering
TABLE_COLOR = (200, 200, 200)
HEADER_COLOR = (100, 100, 255)
CELL_PADDING = 10


def act(conn: ServerConnection):
    lobbies_res = poll_data(conn)

    # TODO: return selection closure, pack as tuple (add additional fields)
    return (lobbies_res.lobbies, )


def render(data, canvas: pygame.Surface):
    lobbies = data[0]
    draw_table(canvas, lobbies)

    # TODO: selection btns


def poll_data(conn: ServerConnection):
    global last_call_time, last_lobbies_res
    current_time = pygame.time.get_ticks()
    if last_lobbies_res is None or current_time - last_call_time >= POLL_INTERVAL_MS:
        last_lobbies_res = list_lobbies_rpc(conn.stub)
        last_call_time = current_time
    return last_lobbies_res


def draw_table(canvas: pygame.Surface, lobbies: Collection[LobbyInfoPublic]):
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
        # TODO: host_player_id -> host_player_name
        for col, key in enumerate(["name", "host_player_id", "player_count", "status"]):
            value = getattr(lobby, key)
            if key == "status":
                value = LobbyStatus.Name(value)
            cell_text = font.render(str(value), True, BLACK_COLOR)
            canvas.blit(cell_text, (col * col_widths[col] + CELL_PADDING, y_offset))
        y_offset += 30

    pygame.draw.rect(canvas, BLACK_COLOR, pygame.Rect(0, 50, CANVAS_RESOLUTION[0], y_offset - 50), 2)
