import pygame

from core.bullet import Bullet
from core.constants import WIDTH, HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, YELLOW, RED, SHOOTING_DELAY_MS


class Spaceship:
    def __init__(self, x, y, image, bullet_color=YELLOW, direction=1):
        self.x = x
        self.y = y
        self.image = image
        self.bullets = []
        self.bullet_color = bullet_color
        self.direction = direction # 1 for right, -1 for left
        self.rect = pygame.Rect(self.x, self.y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        self.last_shot_tick = 0
        self.shoot_delay_ms = SHOOTING_DELAY_MS

    def move(self, dx, dy):
        # Move, but stay within screen bounds
        self.x = min(max(self.x + dx, 0), WIDTH - SPACESHIP_WIDTH)
        self.y = min(max(self.y + dy, 0), HEIGHT - SPACESHIP_HEIGHT)
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (self.x, self.y))
        else:
            if self.bullet_color == RED:
                pygame.draw.rect(surface, (RED), (self.x, self.y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
            else:
                pygame.draw.rect(surface, (YELLOW), (self.x, self.y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
        # Draw all bullets
        for bullet in self.bullets:
            bullet.draw(surface)

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot_tick < self.shoot_delay_ms:
            return
        self.last_shot_tick = now
        # Bullet starts at front of ship
        if self.direction == 1:
            bullet_x = self.x + SPACESHIP_WIDTH
        else:
            bullet_x = self.x - 10 # Left edge for left_firing ship
        bullet_y = self.y + SPACESHIP_HEIGHT//2 - 2

        # Limit max numer of bullets (for challenge!)
        if len(self.bullets) < 3:
            new_bullet = Bullet(bullet_x, bullet_y, self.direction, self.bullet_color)
            self.bullets.append(new_bullet)

    def update_bullets(self):
        for bullet in self.bullets[:]: # Use a shallow copy
            bullet.move()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
