import pygame
import time
from envs.galaxy_env import GalaxyEnv
from core.actions import Actions

def main():
    env = GalaxyEnv(render_mode="human")
    obs, info = env.reset()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()
        aciton = Actions.STAY # default

        if keys[pygame.K_w]:
            action = Actions.UP
        elif keys[pygame.K_s]:
            action = Actions.DOWN
        elif keys[pygame.K_a]:
            action = Actions.LEFT
        elif keys[pygame.K_d]:
            action = Actions.RIGHT
        elif keys[pygame.K_LCTRL]:
            actions = Actions.SHOOT

        obs, reward, terminated, truncated, info = env.step(action)
        env.render()
        time.sleep(0.03) # Smoother animation

    env.close()

if __name__ == "__main__":
    main()