import pygame
from typing import Callable, Tuple, Dict, Optional

from app.utils import unscale_coords
from app.constants.color import BLACK_COLOR


# Styling
DEFAULT_BTN_TXT_COLOR = BLACK_COLOR
DEFAULT_BTN_BG_COLOR = (154, 92, 225)
DEFAULT_BTN_TXT_DISABLED_COLOR = BLACK_COLOR
DEFAULT_BTN_BG_DISABLED_COLOR = (196, 187, 206)


class Button:
    def __init__(
        self,
        id: str,
        text: str,
        pos: Tuple[int, int],
        event_handlers: Dict[str, Callable[[pygame.event.Event], None]],
        handler: Callable[[], None],
        txt_color: Tuple[int, int, int] = DEFAULT_BTN_TXT_COLOR,
        bg_color: Tuple[int, int, int] = DEFAULT_BTN_BG_COLOR,
        txt_color_disabled: Tuple[int, int, int] = DEFAULT_BTN_TXT_DISABLED_COLOR,
        bg_color_disabled: Tuple[int, int, int] = DEFAULT_BTN_BG_DISABLED_COLOR,
        font: str = "Arial",
        font_size: int = 20,
        padding: int = 5,
        fixed_width: Optional[int] = None,
        fixed_height: Optional[int] = None,
    ):
        self.id = id
        self.text = text
        self.pos = pos
        self.handler = handler
        self.font = pygame.font.SysFont(font, font_size)
        self.padding = padding
        self.txt_color = txt_color
        self.bg_color = bg_color
        self.txt_color_disabled = txt_color_disabled or txt_color
        self.bg_color_disabled = bg_color_disabled or bg_color
        self.disabled = False
        self.fixed_width = fixed_width
        self.fixed_height = fixed_height
        surf = self.__build_surf()
        self.rect = surf.get_rect()
        self.rect.topleft = pos
        self.__register_event_handler(event_handlers)


    def draw(
        self,
        canvas: pygame.Surface,
    ):
        surf = self.__build_surf()
        canvas.blit(surf, self.rect)


    def enable(self):
        self.disabled = False


    def disable(self):
        self.disabled = True



    def __register_event_handler(
        self,
        event_handlers: Dict[str, Callable[[pygame.event.Event], None]],
    ):
        event_handlers[self.id] = self.__check_click


    def __check_click(self, event: pygame.event.Event):
        if self.disabled:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            virtual_event_pos = unscale_coords(event.pos)
            if self.rect.collidepoint(virtual_event_pos):
                self.handler()


    def __build_surf(self):
        if self.disabled:
            txt_color = self.txt_color_disabled
            bg_color = self.bg_color_disabled
        else:
            txt_color = self.txt_color
            bg_color = self.bg_color
        text_surface = self.font.render(self.text, True, txt_color)
        text_width, text_height = text_surface.get_size()
        bg_width = self.fixed_width or (text_width + 2 * self.padding)
        bg_height = self.fixed_height or (text_height + 2 * self.padding)
        bg_surface = pygame.Surface((bg_width, bg_height))
        bg_surface.fill(bg_color)
        text_rect = text_surface.get_rect(center=(bg_width // 2, bg_height // 2))
        bg_surface.blit(text_surface, text_rect)
        return bg_surface
