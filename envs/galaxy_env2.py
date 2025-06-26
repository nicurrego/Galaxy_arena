import pygame
import numpy as np
from gym import spaces
from core.actions import Action
from core.constants import HEIGHT, RED, SPACESHIP_HEIGHT, WIDTH, SHOOTING_DELAY_MS
from core.spaceship import Spaceship
from envs.base_galaxy_env import BaseGalaxyEnv

class GalaxyEnv2(BaseGalaxyEnv):
    """Environment for training 2 RL agents playing against each other"""
    def __init__(self, render_mode=None, red_ship_model_path=None):
        super().__init__(render_mode, red_ship_model_path)
        self.yellow_ship = Spaceship(100, HEIGHT//2, None)
        self.red_ship = Spaceship(WIDTH-100, HEIGHT//2, None, bullet_color=RED, direction=-1)
        self.action_space = spaces.Discrete(len(Action))
        obs_len = len(self._get_obs())
        self.observation_space = spaces.Box(low=0, high=255, shape=(obs_len,), dtype=np.int32)

    def reset(self, seed=None, options=None):
        self.yellow_ship.x, self.yellow_ship.y = 100, HEIGHT//2
        self.red_ship.x, self.red_ship.y = WIDTH-100, HEIGHT//2
        self.yellow_health = 1
        self.red_health = 1
        obs = self._get_obs()
        red_obs = self._get_red_ship_obs()
        return (obs, red_obs)
    
    def step(self, yellow_action, red_action):
        # --- Apply yellow ship action ---
        if yellow_action == Action.UP:
            self.yellow_ship.move(0, -5)
        elif yellow_action == Action.DOWN:
            self.yellow_ship.move(0, 5)
        elif yellow_action == Action.LEFT:
            self.yellow_ship.move(-5, 0)
        elif yellow_action == Action.RIGHT:
            self.yellow_ship.move(5, 0)
        elif yellow_action == Action.SHOOT:
            self.yellow_ship.shoot()

        # --- Apply red ship action (flip left/right for red) ---
        if red_action == Action.UP:
            self.red_ship.move(0, -5)
        elif red_action == Action.DOWN:
            self.red_ship.move(0, 5)
        elif red_action == Action.LEFT:
            self.red_ship.move(5, 0)  # Flipped: left for red is right
        elif red_action == Action.RIGHT:
            self.red_ship.move(-5, 0)  # Flipped: right for red is left
        elif red_action == Action.SHOOT:
            self.red_ship.shoot()

        # --- Update all bullets ---
        self.yellow_ship.update_bullets()
        self.red_ship.update_bullets()

        # --- Check for collisions: yellow's bullets hit red ship ---
        red_was_hit = False
        for bullet in self.yellow_ship.bullets[:]:
            if bullet.collides_with(self.red_ship.rect):
                red_was_hit = True
                self.red_health -= 1
                self.yellow_ship.bullets.remove(bullet)

        # --- Check for collisions: red's bullets hit yellow ship ---
        yellow_was_hit = False
        for bullet in self.red_ship.bullets[:]:
            if bullet.collides_with(self.yellow_ship.rect):
                yellow_was_hit = True
                self.yellow_health -= 1
                self.red_ship.bullets.remove(bullet)

        # --- Prepare observations and check for end of episode ---
        obs = self._get_obs()
        red_obs = self._get_red_ship_obs()
        yellow_reward, red_reward = self._calculate_reward(red_was_hit, yellow_was_hit)
        terminated = self.red_health <= 0 or self.yellow_health <= 0
        truncated = False
        info = {}

        # Return both observations for multi-agent use
        return (obs, red_obs), (yellow_reward, red_reward), terminated, truncated, info
    
    def _calculate_reward(self, red_was_hit, yellow_was_hit):
        yellow_reward = 0.001
        red_reward = 0.001

        if red_was_hit:
            yellow_reward += 1.0
            red_reward -= 1.0
        if yellow_was_hit:
            red_reward += 1.0
            yellow_reward -= 1.0
        if self.red_health <= 0:
            yellow_reward += 10.0
            red_reward -= 10.0
        if self.yellow_health <= 0:
            red_reward += 10.0
            yellow_reward -= 10.0

        return yellow_reward, red_reward