from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc.gen.rustic_poker_pb2 import GetLobbiesResponse
from app.rpc import list_lobbies_rpc


def list_lobbies_menu(
    stub: RusticPokerStub,
):
    lobbies: GetLobbiesResponse | None = None
    try:
        lobbies = list_lobbies_rpc(stub)
    except Exception as err:
        print(f"Error:\n{err}")
        return

    print("[Lobbies]")
    print(lobbies)
