import gymnasium as gym
import numpy as np
import pygame
from stable_baselines3 import PPO

from core.constants import SPACESHIP_HEIGHT, WIDTH, HEIGHT, FPS, YELLOW, RED, WHITE, SHOOTING_DELAY_MS
from core.actions import Action
from core.spaceship import Spaceship

class BaseGalaxyEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": FPS}

    def __init__(self, render_mode=None, red_ship_model_path=None):
        super().__init__()
        self.render_mode = render_mode
        self.screen = None
        self.clock = None
        self.red_ship_model_path = red_ship_model_path
        self.red_ship_model = None
        
        if red_ship_model_path:
            try:
                self.red_ship_model = PPO.load(red_ship_model_path)
                print(f"Loaded red ship model from {red_ship_model_path}")
            except Exception as e:
                print(f"Failed to load model: {e}")
                self.red_ship_model = None

        # Initialize ships
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
        return np.array(obs, dtype=np.int32)

    def _get_red_ship_obs(self):
        """Get observation from red ship's perspective"""
        # Helper to flatten bullet positions, pad to max 3 bullets each
        def bullet_obs(bullets):
            obs = []
            for bullet in bullets[:3]:  # Only take max 3 bullets
                obs += [bullet.x, bullet.y]
            # pad if fewer than 3 bullets
            while len(obs) < 6:
                obs.append(-1)  # pad with -1 for x/y if no bullet
            return obs
        
        # Flip the perspective for red ship
        obs = [
            self.red_ship.x, self.red_ship.y,  # Red ship is now "self"
            self.yellow_ship.x, self.yellow_ship.y,  # Yellow ship is now "opponent"
            self.red_health, self.yellow_health,  # Health values flipped
        ]
        obs += bullet_obs(self.red_ship.bullets)  # Red bullets are now "self" bullets
        obs += bullet_obs(self.yellow_ship.bullets)  # Yellow bullets are now "opponent" bullets
        return np.array(obs, dtype=np.int32)

    def reset(self, seed=None, options=None):
        self.yellow_ship.x, self.yellow_ship.y = 100, HEIGHT//4
        self.red_ship.x, self.red_ship.y = WIDTH-100, HEIGHT//2
        self.yellow_health = 2
        self.red_health = 4
        self.yellow_ship.bullets.clear()
        self.red_ship.bullets.clear()
        obs = self._get_obs()
        return obs, {}
    
    def step(self, action):
        # Yellow ship actions
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
        for bullet in self.yellow_ship.bullets[:]:
            if bullet.collides_with(self.red_ship.rect):
                red_was_hit = True
                self.red_health -= 1
                self.yellow_ship.bullets.remove(bullet)

        # Red ship AI behavior - to be implemented by subclasses
        self._update_red_ship()

        # Check for collisions: red's bullets hit yellow ship
        yellow_was_hit = False
        for bullet in self.red_ship.bullets[:]:
            if bullet.collides_with(self.yellow_ship.rect):
                yellow_was_hit = True
                self.yellow_health -= 0
                self.red_ship.bullets.remove(bullet)

        # Prepare observation and check for end of episode
        obs = self._get_obs()
        reward = self._calculate_reward(red_was_hit, yellow_was_hit)
        terminated = self.red_health <= 0 or self.yellow_health <= 0
        truncated = False
        info = {}
        return obs, reward, terminated, truncated, info
    
    def _update_red_ship(self):
        # Base behavior - to be overridden by subclasses
        pass
    
    def _calculate_reward(self, red_was_hit, yellow_was_hit):
        # Base reward calculation - can be overridden
        reward = 0.001  # small reward for surviving
        if red_was_hit:
            reward += 1.0
        if yellow_was_hit:
            reward -= 10.0
        if self.red_health <= 0:
            reward += 10.0  # winning bonus
        if self.yellow_health <= 0:
            reward -= 10.0  # losing penalty
        return reward
    
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

