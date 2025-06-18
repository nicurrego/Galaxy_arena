import gymnasium as gym
import numpy as np
import pygame

from core.constants import WIDTH, HEIGHT, FPS, YELLOW, RED, WHITE, SHOOTING_DELAY_MS
from core.actions import Action
from core.spaceship import Spaceship

class GalaxyEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": FPS}

    def __init__(self, render_mode=None):
        super().__init__()
        pygame.init()
        self.render_mode = render_mode
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # Load images outside and pass them in the runner later!
        self.yellow_ship = Spaceship(100, HEIGHT//2, None)
        self.red_ship = Spaceship(WIDTH-100, HEIGHT//2, None, bullet_color=RED, direction=-1)

        self.observation_space = gym.spaces.Box(
            low=0,
            high=max(WIDTH, HEIGHT),
            shape=(4+2+3*2,),    # shape = 12 = 4 positions + 2 health + 3 bullets each
            dtype=np.int32
        )
        self.action_space = gym.spaces.Discrete(len(Action.all()))

        # Health
        self.yellow_health = 4
        self.red_health = 4

        # Red ship 
        self.red_last_shot_tick = 0
        self.red_shoot_delay_ms = SHOOTING_DELAY_MS * 2

    def reset(self, seed=None, options=None):
        self.yellow_ship.x, self.yellow_ship.y = 100, HEIGHT//2
        self.red_ship.x, self.red_ship.y = WIDTH-100, HEIGHT//2
        self.yellow_health = 4
        self.red_health = 4
        self.yellow_ship.bullets.clear()
        self.red_ship.bullets.clear()
        obs = np.array([self.yellow_ship.x, self.yellow_ship.y, self.red_ship.x, self.red_ship.y], dtype=np.int32)
        return obs, {}
    
    def step(self, action):
        # For now: only move yellow spaceship with the action
        if action == Action.UP:
            self.yellow_ship.move(0, -5)
        elif action == Action.DOWN:
            self.yellow_ship.move(0, 5)
        elif action == Action.LEFT:
            self.yellow_ship.move(-5, 0)
        elif action == Action.RIGHT:
            self.yellow_ship.move(5, 0)
        elif action == Action.SHOOT:
            self.yellow_ship.shoot()

        # Update all bullets
        self.yellow_ship.update_bullets()
        self.red_ship.update_bullets()

        # Check for collisions: yellow's bullets hit red ship
        red_was_hit = False
        for bullet in self.yellow_ship.bullets[:]: # Use a shallow copy
            if bullet.collides_with(self.red_ship.rect):
                red_was_hit = True
                self.red_health -= 1
                self.yellow_ship.bullets.remove(bullet)

        # Red ship can shoot back!
        now = pygame.time.get_ticks()
        if self.yellow_ship.y >= self.red_ship.y:
            if now - self.red_last_shot_tick > self.red_shoot_delay_ms:
                self.red_ship.shoot()
                self.red_last_shot_tick = now       

        # Check for collisions: red's bullets hit yellow ship
        yellow_was_hit = False
        for bullet in self.red_ship.bullets[:]:
            if bullet.collides_with(self.yellow_ship.rect):
                yellow_was_hit = True
                self.yellow_health -= 1
                self.red_ship.bullets.remove(bullet)

        # Prepare observation and check for end of episode
        obs = np.array([self.yellow_ship.x, self.yellow_ship.y, self.red_ship.x, self.red_ship.y], dtype=np.int32)
        reward = 0.1 # for surviving

        if red_was_hit:
            reward += 1.0
        if yellow_was_hit:
            reward -= 1.0
        if self.red_health == 0:
            reward += 10.0 # winning bonus
        if self.yellow_health == 0:
            reward -= 10.0 # losing penalty

        terminated = self.red_health == 0 or self.yellow_health == 0
        truncated = 1 if self.red_health == 0 else -1 if self.yellow_health == 0 else 0
        info = {}
        return obs, reward, terminated, truncated, info
    
    def render(self):
        self.screen.fill((0, 0, 0))
        self.yellow_ship.draw(self.screen)
        self.red_ship.draw(self.screen)

        # Draw health bars
        font = pygame.font.SysFont("comicsans", 30)
        yellow_hp_text = font.render(f"Yellow HP: {self.yellow_health}", 1, WHITE)
        red_hp_text = font.render(f"Red HP: {self.red_health}", 1, WHITE)
        self.screen.blit(yellow_hp_text, (20, 10))
        self.screen.blit(red_hp_text, (WIDTH - red_hp_text.get_width() -20, 10))

        pygame.display.flip()
        self.clock.tick(FPS)

    def close(self):
        pygame.quit()