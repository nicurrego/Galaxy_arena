import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv
from stable_baselines3.common.callbacks import CheckpointCallback

# Instantiate once, at import time
checkpoint_callback = CheckpointCallback(
    save_freq=10_000,
    save_path="./models/",
    name_prefix="ppo_galaxy_model",
)

def main():
    env = GalaxyEnv(render_mode=None)
    model = PPO("MlpPolicy", env, verbose=1)
    # Reuse the global callback
    model.learn(total_timesteps=100_000, callback=checkpoint_callback)

if __name__ == "__main__":
    main()
