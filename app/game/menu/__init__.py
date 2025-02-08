from typing import Literal

from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc import start_lobby_rpc, watch_state_rpc
from .host_lobby import host_lobby_menu
from .join_lobby import join_lobby_menu
from .list_lobbies import list_lobbies_menu
from .respond_matchmaking import respond_matchmaking_menu
from .set_matchmaking_status import set_matchmaking_status_menu
from ..player import PlayerIdentity


def show_main_menu(stub: RusticPokerStub, player: PlayerIdentity):
        while True:
            action = select_action()
            if action == "host-lobby":
                host_lobby_menu(stub, player)
            elif action == "join-lobby":
                join_lobby_menu(stub, player)
            elif action == "list-lobbies":
                list_lobbies_menu(stub)
            elif action == "set-matchmaking-status":
                set_matchmaking_status_menu(stub, player),
            elif action == "respond-matchmaking":
                respond_matchmaking_menu(stub, player)
            elif action == "start-game":
                start_lobby_rpc(stub, player)
            elif action == "watch-game":
                watch_state_rpc(stub, player)
            else:
                break


def select_action() -> Literal["host-lobby", "join-lobby", "list-lobbies", "set-matchmaking-status", "start-game", "watch-game", "quit"]:
    options = [
        "host-lobby",
        "join-lobby",
        "list-lobbies",
        "set-matchmaking-status",
        "respond-matchmaking",
        "start-game",
        "watch-game",
        "quit",
    ]

    while True:
        print(f"Please selection an action:")
        for i, option in enumerate(options, start=0):
            print(f" {i}) {option}")
        user_input = input("> ").strip()

        if user_input.isdigit():
            try:
                index = int(user_input)
                return options[index]
            except (IndexError, ValueError):
                print("Invalid index. Please enter a valid index or action name.")
                continue
        else:
            if user_input in options:
                return user_input
            else:
                print("Invalid action name. Please enter a valid index or action name.")
