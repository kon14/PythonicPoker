import pygame

from pythonic_poker_sdk.types import PokerPhaseEnum
from app.constants.color import WHITE_COLOR
from app.constants.display import CANVAS_RESOLUTION


# Rendering
TABLE_BG_COLOR = (53, 101, 77)
PHASE_TXT_COLOR = WHITE_COLOR


def base_render(
    canvas: pygame.Surface,
    phase: PokerPhaseEnum,
):
    canvas.fill(TABLE_BG_COLOR)
    y_offset = __render_phase_label(canvas, phase, 50)
    y_offset += 20


def __render_phase_label(
    canvas: pygame.Surface,
    phase: PokerPhaseEnum,
    y_offset: int,
):
    font = pygame.font.SysFont("Arial", 30)
    phase_label_txt = font.render(f"{phase}", True, PHASE_TXT_COLOR)
    text_width, text_height = phase_label_txt.get_size()
    x_offset = (CANVAS_RESOLUTION[0] - text_width) // 2
    canvas.blit(phase_label_txt, (x_offset, y_offset))
    return y_offset + text_height
