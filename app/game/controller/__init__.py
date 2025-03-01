import pygame
from typing import List, Optional

from pythonic_poker_sdk import PlayerIdentity, GameState, PokerPhaseEnum, \
    host_lobby_rpc, join_lobby_rpc, set_lobby_matchmaking_status_rpc, respond_lobby_matchmaking_rpc, \
    start_lobby_game_rpc, LobbyInfoPublic
from app.constants.display import CANVAS_RESOLUTION, DISPLAY_RESOLUTION, FRAMES_PER_SECOND
from .view_renderer import game_logic
from .watch_state import start_watch_state_thread
from ..views.types import View, VALID_VIEWS
from ..connection import ServerConnection
from ..events import PythonicPokerEvent


class GameController:
    def __init__(self):
        self.display: pygame.Surface = None  # post-ctor init
        self.canvas: pygame.Surface = None  # post-ctor init
        self.clock = None  # post-ctor init
        self.view: View = "server-selection"
        self.connection: Optional[ServerConnection] = None
        self.player: Optional[PlayerIdentity] = None
        self.view_events: List[pygame.event.Event] = []
        self.running = True
        self.lobby_id: Optional[str] = None
        self.game_state: Optional[GameState] = None


    def start_game(self):
        self.init_pygame()
        self.game_loop()


    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption("PythonicPoker")
        self.display = pygame.display.set_mode(DISPLAY_RESOLUTION)
        self.canvas = pygame.Surface(CANVAS_RESOLUTION)
        self.clock = pygame.time.Clock()
        assert self.display is not None
        assert self.canvas is not None
        assert self.clock is not None


    def game_loop(self):
        while self.running:
            # Handle PyGame Events
            self.handle_events()

            # Clear Surfaces
            self.clear_surfaces()

            # Perform Game Updates:
            game_logic(
                view=self.view,
                set_connection=self.set_connection,
                set_player=self.set_player,
                canvas=self.canvas,
                connection=self.connection,
                player=self.player,
                game_state=self.game_state,
                events=self.view_events.copy(),
            )

            # Render Game
            self.render()

            # Limit FPS
            self.clock.tick(FRAMES_PER_SECOND)


    def handle_events(self):
        self.view_events.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == PythonicPokerEvent.HOST_LOBBY.value:
                try:
                    res: LobbyInfoPublic = host_lobby_rpc(self.connection.stub, self.player, event.lobby_name)
                except Exception as err:
                    print(f"Failed to host lobby ({event.lobby_name})!")
                    print(err)
                    return

                self.lobby_id = res.lobby_id
                self.set_view("lobby")
                start_watch_state_thread(self.connection.stub, self.player)

            elif event.type == PythonicPokerEvent.JOIN_LOBBY.value:
                try:
                    join_lobby_rpc(self.connection.stub, self.player, event.lobby_id)
                except Exception as err:
                    print(f"Failed to join lobby ({event.lobby_id})!")
                    print(err)
                    return
                self.lobby_id = event.lobby_id
                self.set_view("lobby")
                start_watch_state_thread(self.connection.stub, self.player)

            elif event.type == PythonicPokerEvent.LEAVE_LOBBY.value:
                self.lobby_id = None
                # TODO: state stream should end server-side, confirm
                self.set_view("lobby-selection")

            elif event.type == PythonicPokerEvent.SET_VIEW.value:
                self.set_view(event.view)

            elif event.type == PythonicPokerEvent.STATE_UPDATE.value:
                self.game_state = event.state
                print(event.state) # DEBUG
                phase: Optional[PokerPhaseEnum] = PokerPhaseEnum.from_game_state(event.state)
                if phase == PokerPhaseEnum.Ante:
                    self.set_view("poker-ante")
                elif phase == PokerPhaseEnum.Dealing:
                    self.set_view("poker-dealing")
                elif phase == PokerPhaseEnum.FirstBetting:
                    self.set_view("poker-betting")
                elif phase == PokerPhaseEnum.Drawing:
                    self.set_view("poker-drawing")
                elif phase == PokerPhaseEnum.SecondBetting:
                    self.set_view("poker-betting")
                elif phase == PokerPhaseEnum.Showdown:
                    # TODO: stay here until player explicitly leaves or sth
                    self.set_view("poker-showdown")
                else:
                    self.set_view("lobby")

            elif event.type == PythonicPokerEvent.SET_LOBBY_MATCHMAKING.value:
                try:
                    set_lobby_matchmaking_status_rpc(
                        stub=self.connection.stub,
                        player=self.player,
                        matchmaking=event.matchmaking,
                    )
                except Exception as err:
                    print(err)

            elif event.type == PythonicPokerEvent.RESPOND_LOBBY_MATCHMAKING.value:
                try:
                    respond_lobby_matchmaking_rpc(
                        stub=self.connection.stub,
                        player=self.player,
                        accept=event.accept_match,
                    )
                except Exception as err:
                    print(err)

            elif event.type == PythonicPokerEvent.START_LOBBY_MATCH.value:
                try:
                    start_lobby_game_rpc(
                        stub=self.connection.stub,
                        player=self.player,
                    )
                except Exception as err:
                    print(err)

            else:
                self.view_events.append(event)


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
