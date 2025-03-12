import pygame
from google.protobuf.internal.containers import ScalarMap
from typing import Tuple, List, Callable, NamedTuple

from pythonic_poker_sdk.rpc import GameState, LobbyStatus, LobbySettings
from app.components import Button
from app.constants.color import WHITE_COLOR
from app.game.events import PythonicPokerEvent


# Data
event_handlers = {}

# Rendering
BACKGROUND_COLOR = (20, 20, 20)


class LobbyInnerViewRenderArgs(NamedTuple):
    lobby_settings: LobbySettings
    is_lobby_host: bool
    lobby_status: LobbyStatus
    match_may_start: bool
    player_acceptance: ScalarMap[str, bool]
    enable_matchmaking_handler: Callable[[], None]
    disable_matchmaking_handler: Callable[[], None]
    start_match_handler: Callable[[], None]
    accept_match_handler: Callable[[], None]
    decline_match_handler: Callable[[], None]


def act(
    game_state: GameState,
) -> LobbyInnerViewRenderArgs:
    lobby_settings = game_state.lobby_state.settings
    self_id = game_state.self_player_id
    is_lobby_host = game_state.lobby_state.host_player_id == self_id
    lobby_status = game_state.lobby_state.status
    match_may_start = \
        lobby_status is LobbyStatus.MATCHMAKING \
        and len(game_state.lobby_state.game_acceptance) >= lobby_settings.min_players \
        and len(game_state.lobby_state.game_acceptance) == len(game_state.lobby_state.players)
    player_acceptance = game_state.lobby_state.game_acceptance

    enable_matchmaking_handler: Callable[[], None] = lambda : PythonicPokerEvent.set_lobby_matchmaking(matchmaking=True)
    disable_matchmaking_handler: Callable[[], None] = lambda : PythonicPokerEvent.set_lobby_matchmaking(matchmaking=False)
    start_match_handler: Callable[[], None] = lambda : PythonicPokerEvent.start_lobby_match()
    accept_match_handler: Callable[[], None] = lambda : PythonicPokerEvent.respond_lobby_matchmaking(accept_match=True)
    decline_match_handler: Callable[[], None] = lambda : PythonicPokerEvent.respond_lobby_matchmaking(accept_match=False)

    return LobbyInnerViewRenderArgs(
        lobby_settings,
        is_lobby_host,
        lobby_status,
        match_may_start,
        player_acceptance,
        enable_matchmaking_handler,
        disable_matchmaking_handler,
        start_match_handler,
        accept_match_handler,
        decline_match_handler,
    )


def render(args: LobbyInnerViewRenderArgs, canvas: pygame.Surface):
    if args.is_lobby_host:
        __draw_host_ui(
            canvas,
            args.lobby_settings,
            args.lobby_status,
            args.player_acceptance,
            args.match_may_start,
            args.enable_matchmaking_handler,
            args.disable_matchmaking_handler,
            args.start_match_handler,
        )
    else:
        __draw_player_ui(
            canvas,
            args.lobby_settings,
            args.lobby_status,
            args.player_acceptance,
            args.accept_match_handler,
            args.decline_match_handler,
        )


def handle_events(events: List[pygame.event.Event]):
    global event_handlers
    for event in events:
        for handler in event_handlers.values():
            handler(event)


def __draw_host_ui(
    canvas: pygame.Surface,
    lobby_settings: LobbySettings,
    lobby_status: LobbyStatus,
    player_acceptance: ScalarMap[str, bool],
    match_may_start: bool,
    enable_matchmaking_handler: Callable[[], None],
    disable_matchmaking_handler: Callable[[], None],
    start_match_handler: Callable[[], None],
):
    font = pygame.font.SysFont("Arial", 20)
    canvas.fill(BACKGROUND_COLOR)

    starting_y_offset = 60
    y_offset = starting_y_offset
    player_count = len(player_acceptance)

    # Draw Lobby Settings Area
    y_offset = __draw_lobby_settings(canvas, lobby_settings, (100, y_offset))
    y_offset += 80

    # Draw Matchmaking Status Area
    status_label_txt = font.render("Lobby Status:", True, WHITE_COLOR)
    canvas.blit(status_label_txt, (100, y_offset))
    status_value_txt = font.render(LobbyStatus.Name(lobby_status), True, WHITE_COLOR)
    canvas.blit(status_value_txt, (100 + 250, y_offset))
    y_offset += 50

    # Draw Matchmaking Toggle Area
    __draw_enable_matchmaking_btn(
        canvas,
        enable_matchmaking_handler,
        (400, y_offset),
        disabled = lobby_status is LobbyStatus.MATCHMAKING \
                   or player_count < lobby_settings.min_players \
                   or player_count > lobby_settings.max_players,
    )
    __draw_disable_matchmaking_btn(
        canvas,
        disable_matchmaking_handler,
        (700, y_offset),
        disabled = lobby_status is not LobbyStatus.MATCHMAKING,
    )
    y_offset += 100

    # Draw Player Acceptance Area
    y_offset = __draw_player_acceptance(canvas, player_acceptance, (100, y_offset))
    y_offset += 80

    # Draw Start Match Area
    __draw_start_match_btn(
        canvas,
        start_match_handler,
        (600, y_offset),
        disabled=not match_may_start,
    )


def __draw_player_ui(
    canvas: pygame.Surface,
    lobby_settings: LobbySettings,
    lobby_status: LobbyStatus,
    player_acceptance: ScalarMap[str, bool],
    accept_match_handler: Callable[[], None],
    decline_match_handler: Callable[[], None],
):
    font = pygame.font.SysFont("Arial", 20)
    canvas.fill(BACKGROUND_COLOR)

    starting_y_offset = 60
    y_offset = starting_y_offset

    # Draw Lobby Settings Area
    y_offset = __draw_lobby_settings(canvas, lobby_settings, (100, y_offset))
    y_offset += 80

    # Draw Matchmaking Status Area
    status_label_txt = font.render("Lobby Status:", True, WHITE_COLOR)
    canvas.blit(status_label_txt, (100, y_offset))
    status_value_txt = font.render(LobbyStatus.Name(lobby_status), True, WHITE_COLOR)
    canvas.blit(status_value_txt, (100 + 250, y_offset))
    y_offset += 50

    # Draw Matchmaking Response Area
    __draw_accept_matchmaking_btn(
        canvas,
        accept_match_handler,
        (400, y_offset),
        disabled=lobby_status is not LobbyStatus.MATCHMAKING,  # TODO: disable for currently accepted players
    )
    __draw_decline_matchmaking_btn(
        canvas,
        decline_match_handler,
        (700, y_offset),
        disabled=lobby_status is not LobbyStatus.MATCHMAKING,
    )
    y_offset += 100

    # Draw Player Acceptance Area
    y_offset = __draw_player_acceptance(canvas, player_acceptance, (100, y_offset))
    y_offset += 800


def __draw_enable_matchmaking_btn(
    canvas: pygame.Surface,
    enable_matchmaking_handler: Callable[[], None],
    pos: Tuple[int, int],
    disabled: bool,
):
    btn = Button(
        id="btn-lobby-enable-matchmaking",
        text="Enable Matchmaking",
        pos=pos,
        event_handlers=event_handlers,
        handler=enable_matchmaking_handler,
    )
    if disabled:
        btn.disable()
    else:
        btn.enable()
    btn.draw(canvas)


def __draw_disable_matchmaking_btn(
    canvas: pygame.Surface,
    disable_matchmaking_handler: Callable[[], None],
    pos: Tuple[int, int],
    disabled: bool,
):
    btn = Button(
        id="btn-lobby-disable-matchmaking",
        text="Disable Matchmaking",
        pos=pos,
        event_handlers=event_handlers,
        handler=disable_matchmaking_handler,
    )
    if disabled:
        btn.disable()
    else:
        btn.enable()
    btn.draw(canvas)


def __draw_start_match_btn(
    canvas: pygame.Surface,
    start_match_handler: Callable[[], None],
    pos: Tuple[int, int],
    disabled: bool,
):
    btn = Button(
        id="btn-lobby-start-match",
        text="Start Match",
        pos=pos,
        event_handlers=event_handlers,
        handler=start_match_handler,
    )
    if disabled:
        btn.disable()
    else:
        btn.enable()
    btn.draw(canvas)


def __draw_accept_matchmaking_btn(
    canvas: pygame.Surface,
    accept_match_handler: Callable[[], None],
    pos: Tuple[int, int],
    disabled: bool,
):
    btn = Button(
        id="btn-lobby-accept-match",
        text="Accept Match",
        pos=pos,
        event_handlers=event_handlers,
        handler=accept_match_handler,
    )
    if disabled:
        btn.disable()
    else:
        btn.enable()
    btn.draw(canvas)


def __draw_decline_matchmaking_btn(
    canvas: pygame.Surface,
    decline_match_handler: Callable[[], None],
    pos: Tuple[int, int],
    disabled: bool,
):
    btn = Button(
        id="btn-lobby-decline-match",
        text="Decline Match",
        pos=pos,
        event_handlers=event_handlers,
        handler=decline_match_handler,
    )
    if disabled:
        btn.disable()
    else:
        btn.enable()
    btn.draw(canvas)


def __draw_lobby_settings(
    canvas: pygame.Surface,
    lobby_settings: LobbySettings,
    pos: Tuple[int, int],
) -> int:
    font = pygame.font.SysFont("Arial", 20)
    x_offset, y_offset = pos

    game_mode_label_txt = font.render("Game Mode:", True, WHITE_COLOR)
    game_mode_value_txt = font.render(LobbySettings.GameMode.Name(lobby_settings.game_mode), True, WHITE_COLOR)
    ante_amount_label_txt = font.render("Ante Amount:", True, WHITE_COLOR)
    ante_amount_value_txt = font.render(f"{lobby_settings.ante_amount} credits", True, WHITE_COLOR)
    min_players_label_txt = font.render("Minimum Players:", True, WHITE_COLOR)
    min_players_value_txt = font.render(str(lobby_settings.min_players), True, WHITE_COLOR)
    max_players_label_txt = font.render("Maximum Players:", True, WHITE_COLOR)
    max_players_value_txt = font.render(str(lobby_settings.max_players), True, WHITE_COLOR)

    canvas.blit(game_mode_label_txt, (x_offset, y_offset))
    canvas.blit(game_mode_value_txt, (x_offset + 250, y_offset))
    canvas.blit(ante_amount_label_txt, (x_offset + 250 + 300, y_offset))
    canvas.blit(ante_amount_value_txt, (x_offset + 250 + 300 + 250, y_offset))
    y_offset += 30
    canvas.blit(min_players_label_txt, (x_offset, y_offset))
    canvas.blit(min_players_value_txt, (x_offset + 250, y_offset))
    canvas.blit(max_players_label_txt, (x_offset + 250 + 300, y_offset))
    canvas.blit(max_players_value_txt, (x_offset + 250 + 300 + 250, y_offset))

    return y_offset


def __draw_player_acceptance(
    canvas: pygame.Surface,
    player_acceptance: ScalarMap[str, bool],
    pos: Tuple[int, int],
) -> int:
    accepted_players_set = set()
    pending_players_set = set()
    for id, accepted in player_acceptance.items():
        if accepted:
            accepted_players_set.add(id)
        else:
            pending_players_set.add(id)

    font = pygame.font.SysFont("Arial", 20)
    x_offset, y_offset = pos

    accepted_label_txt = font.render("Accepted Players:", True, WHITE_COLOR)
    accepted_label_count_txt = font.render(f"[{len(accepted_players_set)}]", True, WHITE_COLOR)
    pending_label_txt = font.render("Pending Players:", True, WHITE_COLOR)
    pending_label_count_txt = font.render(f"[{len(pending_players_set)}]", True, WHITE_COLOR)

    canvas.blit(accepted_label_txt, (x_offset, y_offset))
    canvas.blit(accepted_label_count_txt, (x_offset + 250, y_offset))
    y_offset += 30
    for player in accepted_players_set:
        player_txt = font.render(f"- {player}", True, WHITE_COLOR)
        canvas.blit(player_txt, (x_offset, y_offset))
        y_offset += 25
    y_offset += 50

    canvas.blit(pending_label_txt, (x_offset, y_offset))
    canvas.blit(pending_label_count_txt, (x_offset + 250, y_offset))
    y_offset += 30
    for player in pending_players_set:
        player_txt = font.render(f"- {player}", True, WHITE_COLOR)
        canvas.blit(player_txt, (x_offset, y_offset))
        y_offset += 25

    return y_offset
