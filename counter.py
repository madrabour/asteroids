import pygame
from constants import SCREEN_WIDTH

class Counter():
    def __init__(self, value):
        self.value = value

    def draw(self, screen):
        font = pygame.font.SysFont("arial", 25)
        text = font.render(str(self.value), True, "white")
        screen.blit(text, (SCREEN_WIDTH - 100, 10) )

