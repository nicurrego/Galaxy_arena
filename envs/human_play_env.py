import gymnasium as gym
import numpy as np
import pygame

from core.constants import SPACESHIP_HEIGHT, WIDTH, HEIGHT, FPS, YELLOW, RED, WHITE, SHOOTING_DELAY_MS
from core.actions import Action
from core.spaceship import Spaceship

class GalaxyEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": FPS}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.init()

        # Load images outside and pass them in the runner later!
        self.yellow_ship = Spaceship(100, HEIGHT//2, None)
        self.red_ship = Spaceship(WIDTH-100, HEIGHT//2, None, bullet_color=RED, direction=-1)

        self.observation_space = gym.spaces.Box(
            low=0,
            high=max(WIDTH, HEIGHT),
            shape=(4+2+3*4,),    # shape = 12 = 4 positions + 2 health + 3*4 bullet cords
            dtype=np.int32
        )
        self.action_space = gym.spaces.Discrete(len(Action.all()))

        # Health
        self.yellow_health = 2
        self.red_health = 4

        # Red ship 
        self.red_last_shot_tick = 0
        self.red_shoot_delay_ms = SHOOTING_DELAY_MS * 2


    def _get_obs(self):
        # Helper to flatten bullet positions, pad to max 3 bullets each
        def bullet_obs(bullets):
            obs = []
            for bullet in bullets[:3]: # Only take max 3 bullets
                obs += [bullet.x, bullet.y]
            # pad if fewer than 3 bullets
            while len(obs) < 6:
                obs.append(-1) # pad with -1 for x/y if no bullet
            return obs
        
        obs = [
            self.yellow_ship.x, self.yellow_ship.y,
            self.red_ship.x, self.red_ship.y,
            self.yellow_health, self.red_health,
        ]
        obs += bullet_obs(self.yellow_ship.bullets)
        obs += bullet_obs(self.red_ship.bullets)
        # print(f"Obs shape: {len(obs)}, Obs: {obs}") # Debug
        return np.array(obs, dtype=np.int32)

    def reset(self, seed=None, options=None):
        self.yellow_ship.x, self.yellow_ship.y = 100, HEIGHT//2
        self.red_ship.x, self.red_ship.y = WIDTH-100, HEIGHT//2
        self.yellow_health = 2
        self.red_health = 4
        self.yellow_ship.bullets.clear()
        self.red_ship.bullets.clear()
        obs = self._get_obs()
        return obs, {}
    
    def step(self, action):
        # Yellow ship actions remain the same
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

        # Enhanced red ship AI
        now = pygame.time.get_ticks()
        
        # Y-axis tracking (existing behavior)
        if (self.yellow_ship.y + SPACESHIP_HEIGHT//2) < self.red_ship.y:
            self.red_ship.move(0, -5)
        elif (self.yellow_ship.y - SPACESHIP_HEIGHT//2) > self.red_ship.y:
            self.red_ship.move(0, 5)
        
        # NEW: X-axis movement - maintain optimal distance
        optimal_distance = WIDTH // 3
        current_distance = self.red_ship.x - self.yellow_ship.x
        if current_distance < optimal_distance - 50:
            self.red_ship.move(5, 0)  # Move away if too close
        elif current_distance > optimal_distance + 50:
            self.red_ship.move(-5, 0)  # Move closer if too far
        
        # NEW: Improved shooting logic
        # Predict where yellow ship will be
        can_shoot = now - self.red_last_shot_tick > self.red_shoot_delay_ms
        yellow_in_line = abs(self.yellow_ship.y - self.red_ship.y) < SPACESHIP_HEIGHT
        
        if can_shoot and (yellow_in_line or np.random.random() < 0.2):
            self.red_ship.shoot()
            self.red_last_shot_tick = now

        # Check for collisions: red's bullets hit yellow ship
        yellow_was_hit = False
        for bullet in self.red_ship.bullets[:]:
            if bullet.collides_with(self.yellow_ship.rect):
                # Comment out or remove the health reduction
                # self.yellow_health -= 1
                yellow_was_hit = True
                self.red_ship.bullets.remove(bullet)

        # Prepare observation and check for end of episode
        obs = self._get_obs()
        reward = 0.001 # for surviving

        if red_was_hit:
            reward += 1.0
        if yellow_was_hit:
            # You can still track hits without damage
            reward -= 0.1  # Reduced penalty for getting hit
        if self.red_health == 0:
            reward += 10.0 # winning bonus
        if self.yellow_health == 0:
            reward -= 10.0 # losing penalty

        terminated = self.red_health == 0 or self.yellow_health == 0
        truncated = 1 if self.red_health == 0 else -1 if self.yellow_health == 0 else 0
        info = {}
        return obs, reward, terminated, truncated, info
    
    def render(self):
        if self.render_mode != "human":
            return
        
        if self.screen is None:
            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            self.clock = pygame.time.Clock()

        self.screen.fill((0, 0, 0))
        self.yellow_ship.draw(self.screen)
        self.red_ship.draw(self.screen)

        # Draw health bars
        font = pygame.font.SysFont("comicsans", 30)
        yellow_hp_text = font.render(f"Yellow HP: {self.yellow_health}", 1, WHITE)
        red_hp_text = font.render(f"Red HP: {self.red_health}", 1, WHITE)
        self.screen.blit(yellow_hp_text, (20, 10))
        self.screen.blit(red_hp_text, (WIDTH - red_hp_text.get_width() - 20, 10))

        pygame.display.flip()
        self.clock.tick(FPS)


    def close(self):
        if self.screen is not None:
            pygame.quit()
            self.screen = None
