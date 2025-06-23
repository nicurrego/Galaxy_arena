import pygame
import numpy as np
from core.constants import SPACESHIP_HEIGHT, WIDTH, SHOOTING_DELAY_MS
from envs.base_galaxy_env import BaseGalaxyEnv

class GalaxyEnv(BaseGalaxyEnv):
    """Environment for training RL agents with enhanced red ship behavior"""
    
    def _update_red_ship(self):
        # Enhanced red ship AI
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
    
    def _calculate_reward(self, red_was_hit, yellow_was_hit):
        reward = 0.001  # small reward for surviving
        
        if red_was_hit:
            reward += 1.0
        if yellow_was_hit:
            reward -= 1.0
        if self.red_health <= 0:
            reward += 10.0  # winning bonus
        if self.yellow_health <= 0:
            reward -= 10.0  # losing penalty
            
        return reward