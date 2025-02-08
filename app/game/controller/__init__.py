import grpc
import os

from app.rpc.gen.rustic_poker_pb2_grpc import RusticPokerStub
from app.rpc import connect_rpc, disconnect_rpc
from ..menu import show_main_menu
from ..player import PlayerIdentity


SERVER_URL_ENV = "SERVER_URL"
DEFAULT_SERVER_URL = "0.0.0.0:55100"


class GameController:
    def __init__(self):
        self.server_url = self.get_server_url()
        self.player = PlayerIdentity()


    def start_game(self):
        with grpc.insecure_channel(self.server_url) as channel:
            stub = RusticPokerStub(channel)
            self.connect(stub)
            show_main_menu(stub, self.player)
            self.disconnect(stub)


    def connect(self, stub: RusticPokerStub):
        connect_rpc(stub, self.player)


    @staticmethod
    def disconnect(stub: RusticPokerStub):
        disconnect_rpc(stub)


    @staticmethod
    def get_server_url() -> str:
        server_url = os.getenv(SERVER_URL_ENV)
        while server_url is None or len(server_url) == 0:
            print(f"Specify RusticPoker gRPC server connection URL: (default: {DEFAULT_SERVER_URL})")
            server_url = input("> ").strip() or DEFAULT_SERVER_URL
        return server_url
