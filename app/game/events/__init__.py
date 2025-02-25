import pygame
from enum import Enum

from pythonic_poker_sdk import GameState
from ..controller.types import View


class PythonicPokerEvent(Enum):
    # Spawns a thread initiating a server-side state stream via RusticPokerStub.WatchState
    ENTER_LOBBY = pygame.USEREVENT + 1
    LEAVE_LOBBY = pygame.USEREVENT + 2
    SET_VIEW = pygame.USEREVENT + 3
    STATE_UPDATE = pygame.USEREVENT + 4


    @staticmethod
    def enter_lobby(lobby_id: str):
        event = pygame.event.Event(PythonicPokerEvent.ENTER_LOBBY.value, lobby_id=lobby_id)
        pygame.event.post(event)


    @staticmethod
    def leave_lobby():
        event = pygame.event.Event(PythonicPokerEvent.LEAVE_LOBBY.value)
        pygame.event.post(event)


    @staticmethod
    def set_view(view: View):
        event = pygame.event.Event(PythonicPokerEvent.SET_VIEW.value, view=view)
        pygame.event.post(event)


    @staticmethod
    def state_update(state: GameState):
        event = pygame.event.Event(PythonicPokerEvent.STATE_UPDATE.value, state=state)
        pygame.event.post(event)
