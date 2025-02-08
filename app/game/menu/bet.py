from typing import Literal
from google.protobuf.empty_pb2 import Empty

from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc import respond_betting_phase_rpc
from app.rpc.gen.rustic_poker_pb2 import RespondBettingPhaseRequest
from ..player import PlayerIdentity


def bet_menu(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    action = select_action()
    success_msg = None
    req = None
    if action == "bet":
        amount = specify_bet_amount()
        req = RespondBettingPhaseRequest(bet=amount)
        success_msg = "Bet placed successfully!"
    elif action == "call":
        req = RespondBettingPhaseRequest(call=Empty())
        success_msg = "Bet called successfully!"
    elif action == "raise":
        amount = specify_bet_amount()
        req = RespondBettingPhaseRequest(raise_bet=amount)
        success_msg = "Bet raised successfully!"
    elif action == "fold":
        req = RespondBettingPhaseRequest(fold=Empty())
        success_msg = "Player folded successfully!"

    try:
        respond_betting_phase_rpc(stub, player, req)

    except Exception as err:
        print(f"Error:\n{err}")
        return

    print(success_msg)


def select_action() -> Literal["bet", "call", "raise", "fold"]:
    options = ["bet", "call", "raise", "fold"]

    while True:
        print(f"Please select an action:")
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


def specify_bet_amount() -> int:
    while True:
        try:
            num = int(input("Specify bet amount: "))
            if num > 0:
                return num
            else:
                print("Please enter a *positive* integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
