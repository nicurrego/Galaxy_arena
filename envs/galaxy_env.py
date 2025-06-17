import gymnasium as gym
import numpy as np
import pygame

from core.constants import WIDTH, HEIGHT, FPS, YELLOW, RED
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
        self.red_ship = Spaceship(WIDTH-100, HEIGHT//2, None)

        self.observation_space = gym.spaces.Box(
            low=0, high=max(WIDTH, HEIGHT), shape=(4,), dtype=np.int32
        )
        self.action_space = gym.spaces.Discrete(len(Action.all()))

    def reset(self, seed=None, options=None):
        self.yellow_ship.x, self.yellow_ship.y = 100, HEIGHT//2
        self.red_ship.x, self.red_ship.y = WIDTH-100, HEIGHT//2
        obs = np.array([self.yellow_ship.x, self.yellow_ship.y, self.red_ship.x, self.red_ship.y], dtype=np.int32)
        return obs, {}
    
    def step(self, action):
        # For now: only move yellow spaceship with the aciton
        if action == Action.UP:
            self.yellow_ship.move(0, -5)
        elif action == Action.DOWN:
            self.yellow_ship.move(0, 5)
        elif action == Action.LEFT:
            self.yellow_ship.move(-5, 0)
        elif action == Action.RIGHT:
            self.yellow_ship.move(5, 0)
        # STAY or SHOOT do nothing for now


        obs = np.array([self.yellow_ship.x, self.yellow_ship.y, self.red_ship.x, self.red_ship.y], dtype=np.int32)
        reward = 0
        terminated = False
        truncated = False
        info = {}
        return obs, reward, terminated, truncated, info
    
    def render(self):
        self.screen.fill((0, 0, 0))
        self.yellow_ship.draw(self.screen)
        self.red_ship.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(FPS)

    def close(self):
        pygame.quit()