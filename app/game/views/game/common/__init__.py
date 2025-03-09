import pygame
from typing import Tuple

from pythonic_poker_sdk.types import PokerPhaseEnum, GameState
from app.constants.color import WHITE_COLOR
from app.constants.display import CANVAS_RESOLUTION
from app.components import Hand


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


def render_players(canvas: pygame.Surface, game_state: GameState):
    # TODO: loop through all players... (centered on self)
    self_player_id = game_state.self_player_id
    player_info = game_state.match_state.player_info.get(self_player_id)
    if player_info:
        player_pos = (500, 500)
        __render_player_info(canvas, player_pos, player_info)


def __render_player_info(
    canvas: pygame.Surface,
    pos: Tuple[int, int],
    player_info: GameState.MatchState.MatchStatePlayerPublicInfo,
):
    # TODO: Render additional info
    hand = Hand.build(player_info.hand_cards)
    if hand:
        hand.draw(canvas, pos)
