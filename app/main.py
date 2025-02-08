import os
import sys

# Set PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.game import GameController


if __name__ == "__main__":
    game = GameController()
    game.start_game()
