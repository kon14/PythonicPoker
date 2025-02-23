from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc.gen.rustic_poker_pb2 import LobbyInfoPublic
from app.rpc import host_lobby_rpc
from ..player import PlayerIdentity


def host_lobby_menu(
    stub: RusticPokerStub,
    player: PlayerIdentity,
):
    lobby_name = None
    while lobby_name is None or len(lobby_name) == 0:
        lobby_name = input("Specify lobby name:\t").strip()

    lobby: LobbyInfoPublic | None = None
    try:
        lobby = host_lobby_rpc(stub, player, lobby_name)

    except Exception as err:
        print(f"Error:\n{err}")
        return

    print("[Lobby]")
    print(lobby)
