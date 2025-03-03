from enum import Enum
from typing import Optional
from google.protobuf.json_format import MessageToDict

from ..rpc import GameState


class PokerPhaseEnum(Enum):
    Ante = 0
    Dealing = 1
    FirstBetting = 2
    Drawing = 3
    SecondBetting = 4
    Showdown = 5


    @staticmethod
    def from_game_state(state: GameState) -> Optional["PokerPhaseEnum"]:
        poker_phase = getattr(getattr(state, "match_state", None), "poker_phase", None)
        if poker_phase is None:
            return None

        # Hacky Workaround (missing optional Proto fields aren't None here...)
        poker_phase_dict = MessageToDict(poker_phase)
        phases = [
            ("ante", PokerPhaseEnum.Ante),
            ("dealing", PokerPhaseEnum.Dealing),
            ("first_betting", PokerPhaseEnum.FirstBetting),
            ("drawing", PokerPhaseEnum.Drawing),
            ("second_betting", PokerPhaseEnum.SecondBetting),
            ("showdown", PokerPhaseEnum.Showdown),
        ]
        for phase_name, phase_enum in phases:
            phase_value = poker_phase_dict.get(phase_name)
            if phase_value is not None:
                return phase_enum
        return None

    def __str__(self):
        return {
            PokerPhaseEnum.Ante: "Ante",
            PokerPhaseEnum.Dealing: "Dealing",
            PokerPhaseEnum.FirstBetting: "First Betting",
            PokerPhaseEnum.Drawing: "Drawing",
            PokerPhaseEnum.SecondBetting: "Second Betting",
            PokerPhaseEnum.Showdown: "Showdown",
        }[self]
