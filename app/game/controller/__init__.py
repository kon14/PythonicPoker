import pygame

from .game_logic import game_logic
from .types import View, VALID_VIEWS
from ..connection import ServerConnection, get_server_connection
from ..player import PlayerIdentity


# Virtual canvas resolution to be used throughout the game.
CANVAS_RESOLUTION = (1280, 720)

# Game window resolution to scale to.
# TODO: via env / resizable etc
DISPLAY_RESOLUTION = (1920, 1080) # or do scaling factor instead ? handle black bars for mismatched aspect ratio

FRAMES_PER_SECOND = 60


class GameController:
    def __init__(self):
        self.display = None
        self.canvas = None
        self.clock = None
        self.view: View | None = None
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

            # Perform Initial Setup
            self.initial_setup()

            # Clear Surfaces
            self.clear_surfaces()

            # Perform Game Updates
            if self.view is not None and self.in_game_view():
                assert self.view is not None
                game_logic(
                    view=self.view,
                    set_view=self.set_view,
                    canvas=self.canvas,
                    connection=self.connection,
                    player=self.player,
                )

            # Render Game
            self.render()

            # Limit FPS
            self.clock.tick(FRAMES_PER_SECOND)


    def initial_setup(self):
        # TODO: refactor for GUI (don't block loop)
        if self.connection is None:
            # Connection Setup
            self.set_view("server-selection")
            self.connection = get_server_connection() # TODO: return nullable res via GUI-aware handler
        elif self.player is None:
            # Player Setup
            self.set_view("player-login")
            self.player = PlayerIdentity() # TODO: return nullable res via GUI-aware handler
        elif self.view is None:
            self.set_view("lobby-selection")


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


    def in_game_view(self):
        return self.view in [None, "server-selection", "player-login"]
