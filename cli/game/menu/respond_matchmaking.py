from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc import respond_lobby_matchmaking_rpc
from ..player import PlayerIdentity


def respond_matchmaking_menu(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    accept: bool or None = None
    while accept is None:
        choice = input("Accept match start (y/n):\t").strip().lower()
        if choice == 'y':
            accept = True
        if choice == 'n':
            accept = False

    try:
        respond_lobby_matchmaking_rpc(stub, player, accept)

    except Exception as err:
        print(f"Error:\n{err}")
        return

    if accept:
        print("Accepted Match Start")
    else:
        print("Declined Match Start")
