import pygame
from typing import Callable, List, Tuple, Optional, NamedTuple

from app.game.events import PythonicPokerEvent
from app.components import Button, TextInput
from app.constants.color import *


# Data
event_handlers = {}

# Rendering
TEXT_INPUT_NAME_DIMENSIONS = (500, 80)


input_txt_lobby_name: Optional[TextInput] = None


class LobbyHostViewRenderArgs(NamedTuple):
    host_lobby_handler: Callable[[str], None]
    cancel_handler: Callable[[], None]


def act():
    host_lobby_handler = lambda lobby_name : __host_lobby(lobby_name)
    cancel_handler = lambda : __cancel()

    return LobbyHostViewRenderArgs(
        host_lobby_handler,
        cancel_handler,
    )


def render(args: LobbyHostViewRenderArgs, canvas: pygame.Surface):
    __draw_form(
        canvas,
        args.host_lobby_handler,
        args.cancel_handler,
    )


def handle_events(events: List[pygame.event.Event]):
    global event_handlers
    for event in events:
        for handler in event_handlers.values():
            handler(event)


def __host_lobby(lobby_name: str):
    global input_txt_lobby_name
    assert input_txt_lobby_name is not None

    PythonicPokerEvent.host_lobby(lobby_name)
    input_txt_lobby_name.clear()


def __cancel():
    global input_txt_lobby_name
    assert input_txt_lobby_name is not None

    input_txt_lobby_name.clear()
    PythonicPokerEvent.set_view("lobby-selection")


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
    btn = Button(
        id="btn-cancel",
        text="< Back",
        pos=pos,
        event_handlers=event_handlers,
        handler=cancel_handler,
    )
    btn.draw(canvas)


def __draw_submit_btn(
    canvas: pygame.Surface,
    host_lobby_handler: Callable[[], None],
    pos: Tuple[int, int],
):
    btn = Button(
        id="btn-lobby-new",
        text="Host Lobby",
        pos=pos,
        event_handlers=event_handlers,
        handler=host_lobby_handler,
    )
    btn.draw(canvas)
