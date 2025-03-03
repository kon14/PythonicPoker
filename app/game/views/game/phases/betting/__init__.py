import pygame

from pythonic_poker_sdk.types import PokerPhaseEnum
from ...common import base_render


def render(
    canvas: pygame.Surface,
):
    base_render(canvas, phase="Betting")  # TODO: ignore hack for now, only used as __str__()
