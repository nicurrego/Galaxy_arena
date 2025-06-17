import pygame
from core.constants import WIDTH, HEIGHT

class Bullet:
    def __init__(self, x, y, direction, color, speed=10):
        self.x = x
        self.y = y
        self.direction = direction  # +1 for right, -1 for left
        self.color = color
        self.speed = speed
        self.width = 10
        self.height = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.x += self.speed * self.direction
        self.rect.x = self.x

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def is_off_screen(self):
        return self.x < 0 or self.x > WIDTH

    # Collision check (to be expanded later)
    def collides_with(self, other_rect):
        return self.rect.colliderect(other_rect)
