from typing import Tuple

from app.constants.display import CANVAS_RESOLUTION, DISPLAY_RESOLUTION


def unscale_coords(pos: Tuple[int, int]) -> Tuple[int, int]:
    scale_x = DISPLAY_RESOLUTION[0] / CANVAS_RESOLUTION[0]
    scale_y = DISPLAY_RESOLUTION[1] / CANVAS_RESOLUTION[1]
    return (pos[0] / scale_x, pos[1] / scale_y)
