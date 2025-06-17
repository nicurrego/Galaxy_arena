import pygame
import time
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from envs.galaxy_env import GalaxyEnv
from core.actions import Action

def main():
    env = GalaxyEnv(render_mode="human")
    obs, info = env.reset()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()
        action = Action.STAY # default

        if keys[pygame.K_w]:
            action = Action.UP
        elif keys[pygame.K_s]:
            action = Action.DOWN
        elif keys[pygame.K_a]:
            action = Action.LEFT
        elif keys[pygame.K_d]:
            action = Action.RIGHT
        elif keys[pygame.K_LCTRL]:
            action = Action.SHOOT

        obs, reward, terminated, truncated, info = env.step(action)
        env.render()
        time.sleep(0.03) # Smoother animation

    env.close()

if __name__ == "__main__":
    main()
