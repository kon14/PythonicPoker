import pygame

from pythonic_poker_sdk.types import PokerPhaseEnum, GameState
from ...common import base_render, render_players


def render(
    canvas: pygame.Surface,
    game_state: GameState,
):
    base_render(canvas, phase=PokerPhaseEnum.Dealing)
    render_players(canvas, game_state)
