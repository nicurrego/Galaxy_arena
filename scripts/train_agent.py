import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv
from stable_baselines3.common.callbacks import CheckpointCallback
import os

checkpoint_callback = CheckpointCallback(
    save_freq=10_000,
    save_path="./models/",
    name_prefix="ppo_galaxy_model_survival_penalty",
)

def main():
    env = GalaxyEnv(render_mode=None)
    model_path = "./models/ppo_galaxy_model_survival_penalty_100000_steps.zip"
    if os.path.exists(model_path):
        print("Resuming from checkpoint:", model_path)
        model = PPO.load(model_path, env=env, verbose=1)
    else:
        print("Starting new model.")
        model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=1_000_000, callback=checkpoint_callback)

if __name__ == "__main__":
    main()