import pygame
import time
from envs.human_play_env import HumanPlayEnv
from core.actions import Action

def main():
    # Use the trained model as the red ship opponent
    red_ship_model_path = "models\ppo_red_ship_Y-axis_movement.zip"
    env = HumanPlayEnv(render_mode="human", red_ship_model_path=red_ship_model_path)
    
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
        elif keys[pygame.K_SPACE]:
            action = Action.SHOOT

        obs, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            print(obs, reward, terminated, truncated, info)
            
            running = False
        env.render()
        time.sleep(0.03) # Smoother animation

    env.close()

if __name__ == "__main__":
    main()
