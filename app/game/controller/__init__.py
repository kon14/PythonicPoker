import pygame

from pythonic_poker_sdk import PlayerIdentity
from app.constants.display import CANVAS_RESOLUTION, DISPLAY_RESOLUTION, FRAMES_PER_SECOND
from .game_logic import game_logic
from .types import View, VALID_VIEWS
from ..connection import ServerConnection, get_server_connection
from ..player import get_peer_address


class GameController:
    def __init__(self):
        self.display = None
        self.canvas = None
        self.clock = None
        self.view: View = "server-selection"
        self.connection: ServerConnection | None = None
        self.player: PlayerIdentity | None = None


    def start_game(self):
        self.init_pygame()
        self.game_loop()


    def init_pygame(self):
        pygame.init()
        self.display = pygame.display.set_mode(DISPLAY_RESOLUTION)
        self.canvas = pygame.Surface(CANVAS_RESOLUTION)
        self.clock = pygame.time.Clock()


    def game_loop(self):
        running = True
        while running:
            # Handle PyGame Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear Surfaces
            self.clear_surfaces()

            # Perform Game Updates:
            game_logic(
                view=self.view,
                set_view=self.set_view,
                set_connection=self.set_connection,
                set_player=self.set_player,
                canvas=self.canvas,
                connection=self.connection,
                player=self.player,
            )

            # Render Game
            self.render()

            # Limit FPS
            self.clock.tick(FRAMES_PER_SECOND)


    def clear_surfaces(self):
        # Clear Screen and Virtual Canvas
        self.display.fill((0, 0, 0))
        self.canvas.fill((0, 0, 0))


    def render(self):
        # Scale Canvas
        scaled_canvas = pygame.transform.scale(self.canvas, DISPLAY_RESOLUTION)
        canvas_placement = (0, 0) # TODO: calculate black bars & placement

        # Blit Display
        self.display.blit(scaled_canvas, canvas_placement)

        # Update Display
        pygame.display.flip()


    def set_view(self, view: View):
        if view not in VALID_VIEWS:
            valid_views = " ".join(VALID_VIEWS)
            raise Exception(f'Invalid view "{view}" provided. Should be one of: {valid_views}')
        self.view = view


    def set_connection(self, conn: ServerConnection):
        self.connection = conn


    def set_player(self, player: PlayerIdentity):
        self.player = player
