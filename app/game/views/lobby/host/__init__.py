import pygame
from typing import Callable, List, Tuple, Optional

from pythonic_poker_sdk import host_lobby_rpc, PlayerIdentity, LobbyInfoPublic
from app.game.connection import ServerConnection
from app.components import Button, TextInput
from app.constants.color import *


# Data
event_handlers = {}

# Rendering
HOST_LOBBY_BTN_BG_COLOR = (0, 255, 50)
CANCEL_BTN_BG_COLOR = (200, 100, 100)
TEXT_INPUT_NAME_DIMENSIONS = (500, 80)


input_txt_lobby_name: Optional[TextInput] = None


def act(
    conn: ServerConnection,
    player: PlayerIdentity,
    on_lobby_host: Callable[[str], None],
    on_cancel: Callable[[], None],
):
    host_lobby = lambda lobby_name : __host_lobby(conn, player, lobby_name, on_lobby_host)
    cancel = lambda : __cancel(on_cancel)
    return (host_lobby, cancel)


def render(data, canvas: pygame.Surface):
    host_lobby = data[0]
    cancel = data[1]
    __draw_form(canvas, host_lobby, cancel)


def handle_events(events: List[pygame.event.Event]):
    global event_handlers
    for event in events:
        for handler in event_handlers.values():
            handler(event)


def __host_lobby(
    conn: ServerConnection,
    player: PlayerIdentity,
    lobby_name: str,
    on_lobby_host: Callable[[str], None],
):
    global input_txt_lobby_name
    assert input_txt_lobby_name is not None

    try:
        res: LobbyInfoPublic = host_lobby_rpc(conn.stub, player, lobby_name)
    except Exception as err:
        print(f"Failed to host lobby ({lobby_name})!")
        print(err)
        return

    input_txt_lobby_name.clear()
    on_lobby_host(res.lobby_id)


def __cancel(on_cancel: Callable[[], None]):
    global input_txt_lobby_name
    assert input_txt_lobby_name is not None

    input_txt_lobby_name.clear()
    on_cancel()


def __draw_form(
    canvas: pygame.Surface,
    host_lobby: Callable[[str], None],
    cancel: Callable[[], None],
):
    global input_txt_lobby_name
    font = pygame.font.SysFont("Arial", 20)
    canvas.fill(WHITE_COLOR)

    starting_y_offset = 60
    y_offset = starting_y_offset

    # Draw Cancel Lobby Button
    __draw_cancel_btn(canvas, cancel, (100, y_offset))

    # Draw Field Label
    text = font.render("Lobby Name:", True, BLACK_COLOR)
    canvas.blit(text, (300, y_offset))
    y_offset += 20 + 10

    # Draw Text Input
    __draw_lobby_name_txt_input(canvas, (300, y_offset))
    assert input_txt_lobby_name is not None
    y_offset += TEXT_INPUT_NAME_DIMENSIONS[1] + 20

    # Draw Submit Button
    host_lobby_handler = lambda : host_lobby(input_txt_lobby_name.get_text())
    __draw_submit_btn(canvas, host_lobby_handler, (500, y_offset))
    input_txt_lobby_name.draw(canvas)


def __draw_lobby_name_txt_input(canvas: pygame.Surface, pos: Tuple[int, int]):
    global input_txt_lobby_name
    if input_txt_lobby_name is None:
        rect = pygame.Rect(pos, TEXT_INPUT_NAME_DIMENSIONS)
        input_txt_lobby_name = TextInput(
            id="txt-input-lobby-name",
            rect=rect,
            max_length=20,
        )
        input_txt_lobby_name.register_event_handler(event_handlers)
    assert input_txt_lobby_name is not None
    input_txt_lobby_name.draw(canvas)


def __draw_cancel_btn(
    canvas: pygame.Surface,
    cancel_handler: Callable[[], None],
    pos: Tuple[int, int],
):
    cancel_btn_surf = Button.build_surf("< Back", BLACK_COLOR, CANCEL_BTN_BG_COLOR, 20, 5)
    cancel_btn = Button(
        id="btn-cancel",
        surf=cancel_btn_surf,
        pos=pos,
        handler=cancel_handler,
    )
    cancel_btn.register_event_handler(event_handlers)
    cancel_btn.draw(canvas)


def __draw_submit_btn(
    canvas: pygame.Surface,
    host_lobby_handler: Callable[[], None],
    pos: Tuple[int, int],
):
    submit_btn_surf = Button.build_surf("Host Lobby", BLACK_COLOR, HOST_LOBBY_BTN_BG_COLOR, 20, 5)
    submit_btn = Button(
        id="btn-lobby-new",
        surf=submit_btn_surf,
        pos=pos,
        handler=host_lobby_handler,
    )
    submit_btn.register_event_handler(event_handlers)
    submit_btn.draw(canvas)
