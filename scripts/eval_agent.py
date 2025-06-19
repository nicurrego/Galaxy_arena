import time
import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv

def main():
    # Path to latest checkpoint
    model_path = ".\models\ppo_galaxy_model_100000_steps.zip"

    # Create env with rendering enabled
    env = GalaxyEnv(render_mode="human")
    model = PPO.load(model_path, env=env)

    episodes = 5
    for ep in range(episodes):
        obs, info = env.reset()
        done = False
        total_reward = 0
        while not done:
            action, _states = model.predict(obs)
            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
            env.render()
            time.sleep(0.03)
            done = terminated or truncated
        print(f"Episode {ep+1}: Total Reward = {total_reward}")
    env.close()

if __name__ == "__main__":
    main()