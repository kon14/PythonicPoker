import pygame
from typing import Tuple, List, Callable

from app.game.events import PythonicPokerEvent
from pythonic_poker_sdk.types import PokerPhaseEnum, GameState
from app.components import Button
from ...common import base_render, render_players


# Data
event_handlers = {}

# Rendering
ACTIONS_POS = (800, 700)


def render(
    canvas: pygame.Surface,
    game_state: GameState,
):
    base_render(canvas, phase="Betting")  # TODO: ignore hack for now, only used as __str__()
    render_players(canvas, game_state)
    poker_phase = game_state.match_state.poker_phase
    bet_btn_disabled = True
    if poker_phase.WhichOneof("phase") == PokerPhaseEnum.FirstBetting:
        if poker_phase.highest_bet_amount is None:
            bet_btn_disabled = False
    else:
        if poker_phase.highest_bet_amount is None:
            bet_btn_disabled = False
    __render_actions(
        canvas=canvas,
        pos=ACTIONS_POS,
        bet_handler=lambda : PythonicPokerEvent.set_view("poker-betting-bet-modal"),
        call_handler=lambda : PythonicPokerEvent.betting_call(),
        raise_handler=lambda : PythonicPokerEvent.set_view("poker-betting-bet-modal"),
        fold_handler=lambda : PythonicPokerEvent.betting_fold(),  # TODO: confirmation view
        bet_btn_disabled=bet_btn_disabled,
    )


def handle_events(events: List[pygame.event.Event]):
    global event_handlers
    for event in events:
        for handler in event_handlers.values():
            handler(event)


def __render_actions(
    canvas: pygame.Surface,
    pos: Tuple[int, int],
    bet_handler: Callable[[], None],
    call_handler: Callable[[], None],
    raise_handler: Callable[[], None],
    fold_handler: Callable[[], None],
    bet_btn_disabled: bool,
):
    btn_width = 100
    gap = 10
    bet_btn_pos = (pos[0], pos[1])
    call_btn_pos = (pos[0] + btn_width + gap, pos[1])
    raise_btn_pos = (pos[0] + (btn_width + gap) * 2, pos[1])
    fold_btn_pos = (pos[0] + (btn_width + gap) * 3, pos[1])
    bet_btn = Button(
        id="btn-bet",
        text="Bet",
        pos=bet_btn_pos,
        event_handlers=event_handlers,
        handler=bet_handler,
        fixed_width=btn_width,
    )
    call_btn = Button(
        id="btn-call",
        text="Call",
        pos=call_btn_pos,
        event_handlers=event_handlers,
        handler=call_handler,
        fixed_width=btn_width,
    )
    raise_btn = Button(
        id="btn-raise",
        text="Raise",
        pos=raise_btn_pos,
        event_handlers=event_handlers,
        handler=raise_handler,
        fixed_width=btn_width,
    )
    fold_btn = Button(
        id="btn-fold",
        text="Fold",
        pos=fold_btn_pos,
        event_handlers=event_handlers,
        handler=fold_handler,
        fixed_width=btn_width,
    )
    if bet_btn_disabled:
        bet_btn.disable()
    else:
        bet_btn.enable()
    bet_btn.draw(canvas)
    call_btn.draw(canvas)
    raise_btn.draw(canvas)
    fold_btn.draw(canvas)
