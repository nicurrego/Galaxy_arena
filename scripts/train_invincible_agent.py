import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv
from stable_baselines3.common.callbacks import CheckpointCallback
import os

checkpoint_callback = CheckpointCallback(
    save_freq=100_000,
    save_path="./models/",
    name_prefix="ppo_rewarded_hits",
)

def main():
    env = GalaxyEnv(render_mode=None)
    
    # Load the existing model
    existing_model_path = "models/ppo_rewarded_hits_500000_steps.zip"
    if os.path.exists(existing_model_path):
        print(f"Loading existing model from {existing_model_path}")
        model = PPO.load(existing_model_path, env=env, verbose=1)
    else:
        print("Starting new model training")
        model = PPO("MlpPolicy", env, verbose=1)
    
    model.learn(total_timesteps=500_000,
                callback=checkpoint_callback,
                 reset_num_timesteps=False)
    
    # Save the final model
    model.save("./models/ppo_rewarded_hits_1M")
    print("Training complete!")

if __name__ == "__main__":
    main()
