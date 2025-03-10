import os
import pygame
from enum import Enum
from typing import Optional, Tuple

from pythonic_poker_sdk import GameState, Card as ProtoCard
from app.constants import ASSET_ROOT


CARD_DIMENSIONS = (60, 84)
SPRITE_ASSET_ROOT = os.path.join(ASSET_ROOT, "img", "cards")

class CardStateEnum(Enum):
    Visible = "visible_card"
    Hidden = "hidden_card"
    Discarded = "discarded_card"


class Card:
    def __init__(self, card: GameState.MatchState.MatchStatePlayerPublicInfo.HandCard):
        self.card: Optional[ProtoCard] = None
        card_variant = card.WhichOneof("card")
        if card_variant == CardStateEnum.Visible.value:
            self.state = CardStateEnum.Visible
            self.card = card.visible_card
            card_rank = ProtoCard.CardRank.Name(card.visible_card.rank)
            card_suit = ProtoCard.CardSuit.Name(card.visible_card.suit)
            sprite_name = f"{card_rank.lower()}_{card_suit.lower()}"
        elif card_variant == CardStateEnum.Hidden.value:
            self.state = CardStateEnum.Hidden
            sprite_name = f"back_blue_basic"
        elif card_variant == CardStateEnum.Discarded.value:
            self.state = CardStateEnum.Discarded
            sprite_name = f"blank_front_with_num_boarders"
        sprite_path = os.path.join(SPRITE_ASSET_ROOT, f"{sprite_name}_white.png")
        self.sprite = pygame.image.load(sprite_path)


    def draw(self, canvas: pygame.Surface, pos: Tuple[int, int]):
        canvas.blit(self.sprite, pos)
