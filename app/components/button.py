import pygame
from typing import Callable, Tuple, Dict

from app.utils import unscale_coords


class Button:
    def __init__(
        self,
        id: str,
        surf: pygame.Surface,
        pos: Tuple[int, int],
        handler: Callable[[], None],
    ):
        self.id = id
        self.surf = surf
        self.rect = surf.get_rect()
        self.rect.topleft = pos
        self.handler = handler


    def draw(self, canvas):
        canvas.blit(self.surf, self.rect)


    def register_event_handler(
        self,
        event_handlers: Dict[str, Callable[[pygame.event.Event], None]],
    ):
        event_handlers[self.id] = self.__check_click


    def __check_click(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            virtual_event_pos = unscale_coords(event.pos)
            if self.rect.collidepoint(virtual_event_pos):
                self.handler()


    @staticmethod
    def build_surf(
        text: str,
        txt_color: Tuple[int, int, int],
        bg_color: Tuple[int, int, int],
        font_size: int,
        padding: int = 0,
    ):
        font = pygame.font.SysFont("Arial", font_size)
        text_surface = font.render(text, True, txt_color)
        text_width, text_height = text_surface.get_size()
        bg_width = text_width + 2 * padding
        bg_height = text_height + 2 * padding
        bg_surface = pygame.Surface((bg_width, bg_height))
        bg_surface.fill(bg_color)
        text_rect = text_surface.get_rect(center=(bg_width // 2, bg_height // 2))
        bg_surface.blit(text_surface, text_rect)
        return bg_surface
