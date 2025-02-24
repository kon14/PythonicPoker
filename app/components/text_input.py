import pygame
from typing import Dict, Callable

from app.utils import unscale_coords
from app.constants.color import BLACK_COLOR


ACTIVE_BG_COLOR = (0, 128, 255)
INACTIVE_BG_COLOR = (200, 200, 200)


class TextInput:
    def __init__(self, id: str, rect: pygame.Rect, max_length: int = 20):
        self._id = id
        self._rect = rect
        self._text = ""
        self._max_length = max_length
        self._active = False
        self.font = pygame.font.SysFont("Arial", 30)


    def register_event_handler(
        self,
        event_handlers: Dict[str, Callable[[pygame.event.Event], None]],
    ):
        event_handlers[self._id] = self.__handle_event


    def draw(self, screen):
        color = ACTIVE_BG_COLOR if self._active else INACTIVE_BG_COLOR
        pygame.draw.rect(screen, color, self._rect, 2)
        text_surface = self.font.render(self._text, True, BLACK_COLOR)
        screen.blit(text_surface, (self._rect.x + 5, self._rect.y + 5))


    def clear(self):
        self._text = ""
        self._active = False


    def get_text(self):
        return self._text


    def __handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            virtual_event_pos = unscale_coords(event.pos)
            if self._rect.collidepoint(virtual_event_pos):
                self._active = True
            else:
                self._active = False

        if event.type == pygame.KEYDOWN:
            if self._active:
                if event.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                elif len(self._text) < self._max_length:
                    self._text += event.unicode
