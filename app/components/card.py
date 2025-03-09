import os
import pygame
from enum import Enum
from typing import Optional, Tuple

from pythonic_poker_sdk import GameState, Card as ProtoCard
from app.constants import ASSET_ROOT


CARD_DIMENSIONS = (60, 84)
SPRITE_ASSET_ROOT = os.path.join(ASSET_ROOT, "img", "cards")

class CardStateEnum(Enum):
    Visible = 0
    Hidden = 1
    Discarded = 2


class Card:
    def __init__(self, card: GameState.MatchState.MatchStatePlayerPublicInfo.HandCard):
        self.card: Optional[ProtoCard] = None
        if card.visible_card:
            self.state = CardStateEnum.Visible
            self.card = card.visible_card
            card_rank = ProtoCard.CardRank.Name(card.visible_card.rank)
            card_suit = ProtoCard.CardSuit.Name(card.visible_card.suit)
            sprite_name = f"{card_rank.lower()}_{card_suit.lower()}"
        elif card.hidden_card:
            self.state = CardStateEnum.Hidden
            sprite_name = f"back_blue_basic"
        elif card.discarded_card:
            self.state = CardStateEnum.Discarded
            sprite_name = f"blank_front_with_num_borders"
        sprite_path = os.path.join(SPRITE_ASSET_ROOT, f"{sprite_name}_white.png")
        self.sprite = pygame.image.load(sprite_path)


    def draw(self, canvas: pygame.Surface, pos: Tuple[int, int]):
        canvas.blit(self.sprite, pos)
