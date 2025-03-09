import pygame
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer
from typing import Tuple, Optional

from pythonic_poker_sdk.rpc import GameState
from .card import Card, CARD_DIMENSIONS


GAP_X_PX = 5


class Hand:
    def __init__(
        self,
        cards: RepeatedCompositeFieldContainer[GameState.MatchState.MatchStatePlayerPublicInfo.HandCard]
    ):
        self.cards = []
        for card in cards:
            card_obj = Card(card)
            self.cards.append(card_obj)


    def build(cards: RepeatedCompositeFieldContainer[GameState.MatchState.MatchStatePlayerPublicInfo.HandCard]) -> Optional["Hand"]:
        if len(cards) == 0:
            return None
        return Hand(cards)


    def draw(self, canvas: pygame.Surface, pos: Tuple[int, int]):
        for card in self.cards:
            card.draw(canvas, pos)
            pos = [pos[0] + CARD_DIMENSIONS[0] + GAP_X_PX, pos[1]]
