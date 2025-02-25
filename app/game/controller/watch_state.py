import threading
import pygame

from pythonic_poker_sdk import RusticPokerStub, PlayerIdentity, watch_state_rpc
from ..events import PythonicPokerEvent


def start_watch_state_thread(stub: RusticPokerStub, player: PlayerIdentity):
    grpc_thread = threading.Thread(target=__watch_state_event_stream, args=(stub, player))
    grpc_thread.daemon = True  # kill thread on main program exit
    grpc_thread.start()


def __watch_state_event_stream(stub, player):
    for state in watch_state_rpc(stub, player):
        stream_event = pygame.event.Event(PythonicPokerEvent.STATE_UPDATE.value, state=state)
        pygame.event.post(stream_event)
