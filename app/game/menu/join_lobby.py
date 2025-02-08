from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc import join_lobby_rpc, watch_state_rpc
from ..player import PlayerIdentity


def join_lobby_menu(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    lobby_id = None
    while lobby_id is None or len(lobby_id) == 0:
        lobby_id = input("Specify lobby id:\t").strip()

    try:
        join_lobby_rpc(stub, player, lobby_id)

    except Exception as err:
        print(f"Error:\n{err}")
        return

    print("Lobby joined successfully!")
