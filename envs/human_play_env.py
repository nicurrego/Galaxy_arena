import pygame
import numpy as np
from envs.base_galaxy_env import BaseGalaxyEnv
from core.constants import WIDTH, HEIGHT, SPACESHIP_HEIGHT
from core.actions import Action

class HumanPlayEnv(BaseGalaxyEnv):
    """Environment for human play with immediate pygame initialization"""
    
    def __init__(self, render_mode="human"):
        super().__init__(render_mode=render_mode)
        # Initialize pygame immediately for human play
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
    
    def _update_red_ship(self):
        # Use the same model-based approach as GalaxyEnv
        if self.red_ship_model:
            red_obs = self._get_red_ship_obs()
            action, _ = self.red_ship_model.predict(red_obs)
            
            # Apply action (flipping directions as needed)
            if action == Action.UP:
                self.red_ship.move(0, -5)
            elif action == Action.DOWN:
                self.red_ship.move(0, 5)
            elif action == Action.LEFT:
                self.red_ship.move(5, 0)  # Flipped: left for red is right
            elif action == Action.RIGHT:
                self.red_ship.move(-5, 0)  # Flipped: right for red is left
            elif action == Action.SHOOT:
                self.red_ship.shoot()
        else:
            # Fallback to enhanced red ship AI
            # (same as in GalaxyEnv)
            now = pygame.time.get_ticks()
            # ... rest of the fallback code
