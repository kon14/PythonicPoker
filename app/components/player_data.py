import pygame
from typing import Tuple, Optional

from pythonic_poker_sdk.types import GameState
from app.components import Hand
from app.constants.color import WHITE_COLOR

BOARD_DIMENSIONS = (300, 60)
DATA_DIMENSIONS = (Hand.get_size()[0], (Hand.get_size()[1] * 8 / 10) + BOARD_DIMENSIONS[1])
BOARD_BORDER_WIDTH = 3  # border-boX
PLAYER_NAME_TXT_COLOR = WHITE_COLOR
PLAYER_BET_TXT_COLOR = (237, 197, 85)
BOARD_BG_COLOR = (92, 55, 86)
ACTIVE_BORDER_COLOR = (209, 176, 44)
INACTIVE_BORDER_COLOR = (176, 172, 157)


class PlayerData:
    def __init__(
        self,
        player_id: str,
        match_state: GameState.MatchState,
    ):
        player_info = match_state.player_info.get(player_id)
        self.hand: Optional[Hand] = Hand.build(player_info.hand_cards)
        self.active = player_id in match_state.active_player_ids
        self.player_name: str = player_info.player_name
        self.bet_amount = match_state.player_bet_amounts.get(player_id, 0)


    def draw(
        self,
        canvas: pygame.Surface,
        pos: Tuple[int, int],
    ):
        # Draw Hand
        if self.hand:
            self.hand.draw(canvas, pos)
        # Draw Board
        hand_surf_dimensions = Hand.get_size()
        x_offset = (hand_surf_dimensions[0] - BOARD_DIMENSIONS[0]) // 2
        y_offset = hand_surf_dimensions[1] * 8 // 10  # slight overlap
        pos = (pos[0] + x_offset, pos[1] + y_offset)
        self.__draw_board(canvas, pos)


    def __draw_board(
        self,
        canvas: pygame.Surface,
        pos: Tuple[int, int],
    ):
        # Draw Board Border
        border_color = ACTIVE_BORDER_COLOR if self.active else INACTIVE_BORDER_COLOR
        pygame.draw.rect(canvas, border_color, (pos, BOARD_DIMENSIONS))
        # Draw Board
        inner_pos = (pos[0] + BOARD_BORDER_WIDTH, pos[1] + BOARD_BORDER_WIDTH)
        inner_dimensions = (BOARD_DIMENSIONS[0] - 2 * BOARD_BORDER_WIDTH, BOARD_DIMENSIONS[1] - 2 * BOARD_BORDER_WIDTH)
        pygame.draw.rect(canvas, BOARD_BG_COLOR, (inner_pos, inner_dimensions))
        # Draw Name
        player_name_pos = (pos[0] + 10, pos[1] + 5)
        player_name_font = pygame.font.SysFont("Arial", 30)
        player_name_txt = player_name_font.render(self.player_name, True, PLAYER_NAME_TXT_COLOR)
        canvas.blit(player_name_txt, player_name_pos)
        # Draw Bet Amount
        bet_amount_pos = (pos[0] + 10, pos[1] + 40)
        # TODO: credits icon
        bet_amount_font = pygame.font.SysFont("Arial", 15)
        bet_amount_txt = bet_amount_font.render(f"{self.bet_amount}", True, PLAYER_BET_TXT_COLOR)
        canvas.blit(bet_amount_txt, bet_amount_pos)
