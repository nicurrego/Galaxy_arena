import pygame

from core.bullet import Bullet
from core.constants import WIDTH, HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, YELLOW, RED


class Spaceship:
    def __init__(self, x, y, image, bullet_color=YELLOW, direction=1):
        self.x = x
        self.y = y
        self.image = image
        self.bullets = []
        self.bullet_color = bullet_color
        self.direction = direction # 1 for right, -1 for left
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
        # Draw all bullets
        for bullet in self.bullets:
            bullet.draw(surface)

    def shoot(self):
        # Bullet starts at front of ship
        if self.directin == 1:
            bullet_x = self.x + SPACESHIP_WIDTH
        else:
            bullet_x = self.x - 10 # Left edge for left_firing ship
        bullet_y = self.y + SPACESHIP_HEIGHT//2 - 2

        # Limit max numer of bullets (for challenge!)
        if len(self.bullets) < 3:
            new_bullet = Bullet(bullet_x, bullet_y, self.direction, self.bullet_color)
            self.bullets.append(new_bullet)
