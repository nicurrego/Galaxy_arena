import pygame
import numpy as np
from core.actions import Action
from core.constants import SPACESHIP_HEIGHT, WIDTH, SHOOTING_DELAY_MS
from envs.base_galaxy_env import BaseGalaxyEnv

class GalaxyEnv(BaseGalaxyEnv):
    """Environment for training RL agents with enhanced red ship behavior"""
    
    def _update_red_ship(self):
        # If we have a trained model for red ship, use it
        if self.red_ship_model:
            # Create observation from red ship's perspective (flipped)
            red_obs = self._get_red_ship_obs()
            
            # Get action from model
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

    def _calculate_reward(self, red_was_hit, yellow_was_hit):
        reward = -0.001  # small reward for surviving
        
        if red_was_hit:
            reward += 5.0
        if yellow_was_hit:
            reward -= 10.0
        if self.red_health <= 0:
            reward += 5.0  # winning bonus
        if self.yellow_health <= 0:
            reward -= 0.01  # losing penalty
            
        return reward
