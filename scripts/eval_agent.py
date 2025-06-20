import time
import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv
from utils.logger import log_to_csv

def main():
    # Path to latest checkpoint
    model_path = ".\models\ppo_galaxy_model_survival_penalty_100000_steps.zip"

    # Create env with rendering enabled
    env = GalaxyEnv(render_mode="human")
    model = PPO.load(model_path, env=env)

    episodes = 5
    total_rewards = []
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
        total_rewards.append(total_reward)
        print(f"Episode {ep+1}: Total Reward = {total_reward}")
    env.close()

    # Log to CSV
    log_to_csv(
        filepath="logs/experiment_results.csv",
        model=model_path,
        episodes=episodes,
        rewards=total_rewards,
        notes="Agent trained with survival penalty of -0.001."
    )
    print("Evaluation logged in CSV.")

if __name__ == "__main__":
    main()