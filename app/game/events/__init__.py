import pygame
from enum import Enum

from pythonic_poker_sdk import GameState
from ..views.types import View


class PythonicPokerEvent(Enum):
    # Spawns a thread initiating a server-side state stream via RusticPokerStub.WatchState
    HOST_LOBBY = pygame.USEREVENT + 1
    JOIN_LOBBY = pygame.USEREVENT + 2
    LEAVE_LOBBY = pygame.USEREVENT + 3
    SET_VIEW = pygame.USEREVENT + 4
    STATE_UPDATE = pygame.USEREVENT + 5
    SET_LOBBY_MATCHMAKING = pygame.USEREVENT + 6
    RESPOND_LOBBY_MATCHMAKING = pygame.USEREVENT + 7
    START_LOBBY_MATCH = pygame.USEREVENT + 8


    @staticmethod
    def host_lobby(lobby_name: str):
        event = pygame.event.Event(PythonicPokerEvent.HOST_LOBBY.value, lobby_name=lobby_name)
        pygame.event.post(event)


    @staticmethod
    def join_lobby(lobby_id: str):
        event = pygame.event.Event(PythonicPokerEvent.JOIN_LOBBY.value, lobby_id=lobby_id)
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


    @staticmethod
    def set_lobby_matchmaking(matchmaking: bool):
        event = pygame.event.Event(PythonicPokerEvent.SET_LOBBY_MATCHMAKING.value, matchmaking=matchmaking)
        pygame.event.post(event)


    @staticmethod
    def respond_lobby_matchmaking(accept_match: bool):
        event = pygame.event.Event(PythonicPokerEvent.RESPOND_LOBBY_MATCHMAKING.value, accept_match=accept_match)
        pygame.event.post(event)


    @staticmethod
    def start_lobby_match():
        event = pygame.event.Event(PythonicPokerEvent.START_LOBBY_MATCH.value)
        pygame.event.post(event)
