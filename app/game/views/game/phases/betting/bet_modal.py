import pygame
from typing import Tuple, List, Optional, Literal, Callable

from app.game.events import PythonicPokerEvent
from pythonic_poker_sdk.types import PokerPhaseEnum, GameState
from app.components import Button, TextInput
from app.constants.color import BLACK_COLOR, WHITE_COLOR
from app.constants.display import CANVAS_RESOLUTION


# Data
event_handlers = {}

# Rendering
TEXT_INPUT_BET_AMOUNT_DIMENSIONS = (500, 80)


input_txt_bet_amount: Optional[TextInput] = None


def render(
    canvas: pygame.Surface,
    game_state: GameState,
):
    input_amount = __get_input_amount_int()
    poker_phase = game_state.match_state.poker_phase
    bet_type: Literal["bet", "raise"] = "bet"
    current_bet_amount = 0
    if poker_phase.WhichOneof("phase") == PokerPhaseEnum.FirstBetting:
        if poker_phase.highest_bet_amount is not None:
            bet_type = "raise"
            current_bet_amount = poker_phase.highest_bet_amount
    else:
        if poker_phase.highest_bet_amount is not None:
            bet_type = "raise"
            current_bet_amount = poker_phase.highest_bet_amount
    # Obscure Existing Canvas Content
    overlay_surf = pygame.Surface(canvas.get_size())
    overlay_surf.fill(BLACK_COLOR)
    overlay_surf.set_alpha(128)
    canvas.blit(overlay_surf, (0, 0))
    # Draw Text Input
    bet_amount_pos = ((CANVAS_RESOLUTION[0] - TEXT_INPUT_BET_AMOUNT_DIMENSIONS[0]) // 2, 500)
    __draw_bet_amount_txt_input(canvas, pos=bet_amount_pos)
    # Validation
    submit_btn_disabled = True
    if (input_amount) > current_bet_amount:
        submit_btn_disabled = False
    # TODO: Display validation messages
    # Draw Action Buttons
    action_btns_pos = ((CANVAS_RESOLUTION[0] - TEXT_INPUT_BET_AMOUNT_DIMENSIONS[0]) // 2, 600)
    __draw_action_btns(
        canvas=canvas,
        pos=action_btns_pos,
        bet_type=bet_type,
        submit_btn_disabled=submit_btn_disabled,
        submit_handler=lambda : PythonicPokerEvent.betting_bet(input_amount),
        cancel_handler=lambda : PythonicPokerEvent.set_view("poker-betting")
    )


def handle_events(events: List[pygame.event.Event]):
    global event_handlers
    for event in events:
        for handler in event_handlers.values():
            handler(event)


def __draw_bet_amount_txt_input(canvas: pygame.Surface, pos: Tuple[int, int]):
    # TODO: only allow digits (via regexp)
    global input_txt_bet_amount
    if input_txt_bet_amount is None:
        rect = pygame.Rect(pos, TEXT_INPUT_BET_AMOUNT_DIMENSIONS)
        input_txt_bet_amount = TextInput(
            id="txt-input-bet-amount",
            rect=rect,
            max_length=20,
            txt_color=WHITE_COLOR,
        )
        input_txt_bet_amount.register_event_handler(event_handlers)
    assert input_txt_bet_amount is not None
    input_txt_bet_amount.draw(canvas)


def __draw_action_btns(
    canvas: pygame.Surface,
    pos: Tuple[int, int],
    bet_type: Literal["bet", "raise"],
    submit_btn_disabled: bool,
    submit_handler: Callable[[], None],
    cancel_handler: Callable[[], None],
):
    submit_btn_txt = "Bet" if bet_type == "bet" else "Raise"
    submit_btn = Button(
        id="btn-bet-submit",
        text=submit_btn_txt,
        pos=pos,
        event_handlers=event_handlers,
        handler=submit_handler,
    )
    cancel_btn = Button(
        id="btn-bet-submit",
        text="Cancel",
        pos=pos,
        event_handlers=event_handlers,
        handler=cancel_handler,
        # TODO: alt-color
    )
    if submit_btn_disabled:
        submit_btn.disable()
    else:
        submit_btn.enable()
    submit_btn.draw(canvas)
    cancel_btn.draw(canvas)


def __get_input_amount_int() -> Optional[int]:
    global input_txt_bet_amount
    amount_str = input_txt_bet_amount.get_text()
    if amount_str == "":
        return None
    try:
        return int(amount_str)
    except ValueError:
        return None
