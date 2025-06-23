import pygame
import numpy as np
from envs.base_galaxy_env import BaseGalaxyEnv
from core.constants import WIDTH, HEIGHT, SPACESHIP_HEIGHT

class HumanPlayEnv(BaseGalaxyEnv):
    """Environment for human play with immediate pygame initialization"""
    
    def __init__(self, render_mode="human"):
        super().__init__(render_mode=render_mode)
        # Initialize pygame immediately for human play
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
    
    def _update_red_ship(self):
        # Use the same enhanced red ship behavior as in GalaxyEnv
        now = pygame.time.get_ticks()
        
        # Y-axis tracking
        if (self.yellow_ship.y + SPACESHIP_HEIGHT//2) < self.red_ship.y:
            self.red_ship.move(0, -5)
        elif (self.yellow_ship.y - SPACESHIP_HEIGHT//2) > self.red_ship.y:
            self.red_ship.move(0, 5)
        
        # X-axis movement - maintain optimal distance
        optimal_distance = WIDTH // 3
        current_distance = self.red_ship.x - self.yellow_ship.x
        if current_distance < optimal_distance - 50:
            self.red_ship.move(5, 0)  # Move away if too close
        elif current_distance > optimal_distance + 50:
            self.red_ship.move(-5, 0)  # Move closer if too far
        
        # Improved shooting logic
        can_shoot = now - self.red_last_shot_tick > self.red_shoot_delay_ms
        yellow_in_line = abs(self.yellow_ship.y - self.red_ship.y) < SPACESHIP_HEIGHT
        
        if can_shoot and (yellow_in_line or np.random.random() < 0.2):
            self.red_ship.shoot()
            self.red_last_shot_tick = now