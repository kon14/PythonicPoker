import os
import sys
import grpc
import pygame

from pythonic_poker_sdk import RusticPokerStub


SERVER_URL_ENV = "SERVER_URL"
DEFAULT_SERVER_URL = "0.0.0.0:55100"


class ServerConnection:
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.channel = grpc.insecure_channel(self.server_url)
        self.stub = RusticPokerStub(self.channel)
        self._monitor_channel_state()


    def _monitor_channel_state(self):
        def on_state_change(state):
            if state == grpc.ChannelConnectivity.SHUTDOWN:
                self._handle_channel_shutdown()

        self.channel.subscribe(on_state_change)


    def _handle_channel_shutdown(self):
        # TODO: handle gracefully
        print("Lost server connection!")
        pygame.quit()
        sys.exit()


    @staticmethod
    def health_check_server(server_url: str):
        # TODO
        pass


    @staticmethod
    def get_server_url_via_env() -> str | None:
        server_url = os.getenv(SERVER_URL_ENV)
        if server_url is None or len(server_url.strip()) == 0:
            return None
        return server_url.strip()


def get_server_connection() -> ServerConnection:
    server_url = ServerConnection.get_server_url_via_env()
    conn = None

    while conn is None:
        # TODO: UI-based selection fallback #
        while server_url is None or len(server_url) == 0:
            print(f"Specify RusticPoker gRPC server connection URL: (default: {DEFAULT_SERVER_URL})")
            server_url = input("> ").strip() or DEFAULT_SERVER_URL
        #####################################
        try:
            ServerConnection.health_check_server(server_url)
            conn = ServerConnection(server_url)
        except Exception:
            continue

    return conn
