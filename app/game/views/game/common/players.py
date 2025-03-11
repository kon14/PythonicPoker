import pygame
from google.protobuf.internal.containers import RepeatedScalarFieldContainer
from copy import deepcopy
from typing import Tuple, Dict, List

from pythonic_poker_sdk.types import GameState
from app.components import PlayerData, DATA_DIMENSIONS
from app.constants.display import CANVAS_RESOLUTION


CANVAS_CENTER_X = CANVAS_RESOLUTION[0] // 2
CANVAS_CENTER_Y = CANVAS_RESOLUTION[0] // 2
MINIMUM_PADDING = 50

P_X0 = MINIMUM_PADDING
P_X1 = (CANVAS_CENTER_X - DATA_DIMENSIONS[0]) // 2
P_X2 = CANVAS_CENTER_X - DATA_DIMENSIONS[0] // 2
P_X3 = CANVAS_RESOLUTION[0] - ((CANVAS_CENTER_X - DATA_DIMENSIONS[0]) // 2) - DATA_DIMENSIONS[0]
P_X4 = CANVAS_RESOLUTION[0] - DATA_DIMENSIONS[0] - MINIMUM_PADDING

P_Y0 = MINIMUM_PADDING
P_Y1 = (CANVAS_CENTER_Y - DATA_DIMENSIONS[1]) // 2
P_Y2 = CANVAS_CENTER_Y - DATA_DIMENSIONS[1] // 2
P_Y3 = CANVAS_RESOLUTION[1] - ((CANVAS_CENTER_Y - DATA_DIMENSIONS[1]) // 2) - DATA_DIMENSIONS[1]
P_Y4 = CANVAS_RESOLUTION[1] - DATA_DIMENSIONS[1] - MINIMUM_PADDING

PLAYER_POSITIONS: Dict[int, List[Tuple[int, int]]] = {
    # TODO: Improve placement (7x7)
    2: [(P_X2, P_Y4), (P_X2, P_Y0)],
    3: [(P_X2, P_Y4), (P_X1, P_Y0), (P_X3, P_Y0)],
    4: [(P_X2, P_Y4), (P_X0, P_Y2), (P_X2, P_Y0), (P_X4, P_Y2)],
    5: [(P_X2, P_Y4), (P_X0, P_Y2), (P_X1, P_Y0), (P_X3, P_Y0), (P_X4, P_Y2)],
    6: [(P_X2, P_Y4), (P_X1, P_Y3), (P_X1, P_Y2), (P_X2, P_Y0), (P_X4, P_Y2), (P_X4, P_Y3)],
    7: [(P_X2, P_Y4), (P_X1, P_Y3), (P_X1, P_Y2), (P_X1, P_Y0), (P_X3, P_Y0), (P_X4, P_Y2), (P_X4, P_Y3)],
    8: [(P_X2, P_Y4), (P_X1, P_Y3), (P_X1, P_Y2), (P_X1, P_Y1), (P_X2, P_Y0), (P_X4, P_Y1), (P_X4, P_Y2), (P_X4, P_Y3)],
}


def render_players(canvas: pygame.Surface, game_state: GameState):
    player_queue = __get_player_queue(game_state)
    player_positions = PLAYER_POSITIONS.get(len(game_state.lobby_state.players))
    for i, player_id in enumerate(player_queue):
        player_info = game_state.match_state.player_info.get(player_id)
        if player_info:
            pos = player_positions[i]
            player_data = PlayerData(player_id, game_state.match_state)
            player_data.draw(canvas, pos)


def __get_player_queue(game_state: GameState) -> RepeatedScalarFieldContainer[str]:
    self_player_id = game_state.self_player_id
    table_players_order = deepcopy(game_state.match_state.table_players_order)
    while True:
        if table_players_order[0] == self_player_id:
            return table_players_order
        else:
            head = table_players_order.pop()
            table_players_order.append(head)
