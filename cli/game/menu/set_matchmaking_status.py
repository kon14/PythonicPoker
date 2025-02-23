from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc import set_lobby_matchmaking_status_rpc
from ..player import PlayerIdentity


def set_matchmaking_status_menu(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    matchmaking: bool or None = None
    while matchmaking is None:
        choice = input("Enable matchmaking (y/n):\t").strip().lower()
        if choice == 'y':
            matchmaking = True
        if choice == 'n':
            matchmaking = False

    try:
        set_lobby_matchmaking_status_rpc(stub, player, matchmaking)

    except Exception as err:
        print(f"Error:\n{err}")
        return

    if matchmaking:
        print("Enabled Lobby Matchmaking")
    else:
        print("Disabled Lobby Matchmaking")
