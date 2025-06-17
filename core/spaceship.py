# core/spaceship.py

import pygame
from core.constants import WIDTH, HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT

class Spaceship:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    def move(self, dx, dy):
        # Move, but stay within screen bounds
        self.x = min(max(self.x + dx, 0), WIDTH - SPACESHIP_WIDTH)
        self.y = min(max(self.y + dy, 0), HEIGHT - SPACESHIP_HEIGHT)
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(surface, (255, 255, 0), (self.x, self.y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
