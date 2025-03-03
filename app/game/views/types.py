from typing import Literal

# TODO: refactor as Enum + __str__() override

View = Literal[
    # Initial Setup
    "server-selection",
    "player-login",
    # Pre-Game
    "lobby-selection",
    "lobby-creation",
    "lobby",
    # In-Game
    "poker-ante",
    "poker-dealing",
    "poker-betting",
    "poker-drawing",
    "poker-showdown",
]

VALID_VIEWS = [
    # Initial Setup
    "server-selection",
    "player-login",
    # Pre-Game
    "lobby-selection",
    "lobby-creation",
    "lobby",
    # In-Game
    "poker-ante",
    "poker-dealing",
    "poker-betting",
    "poker-drawing",
    "poker-showdown",
]
