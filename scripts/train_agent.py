import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv
from stable_baselines3.common.callbacks import CheckpointCallback
import os

algorithm = 'ppo'
model_name = 'B'
model_number = '04'

checkpoint_callback = CheckpointCallback(
    save_freq=250_000,
    save_path="./models/",
    name_prefix=algorithm+'_'+model_name+'_'+model_number,
)

def main():
    # model to set as red ship
    red_ship_model_path = "."
    env = GalaxyEnv(render_mode=None, red_ship_model_path=red_ship_model_path)
    
    # Load the existing model to continue training
    existing_model_path = "none"
    if os.path.exists(existing_model_path):
        print(f"Loading existing model from {existing_model_path}")
        model = PPO.load(existing_model_path, env=env, verbose=1)
    else:
        print("Starting new model training")
        model = PPO("MlpPolicy", env, verbose=1)
    
    if red_ship_model_path:
        print(f"red ship agent is being used for training/nmodel: {red_ship_model_path}")
    else:
        print(f"Baseline model for the red ship is being used for training")
    model.learn(total_timesteps=300_000,
                callback=checkpoint_callback,
                 reset_num_timesteps=False)
    
    # Save the final model
    model.save("./models/"+model_name+'_'+model_number)
    print("Training complete!")

if __name__ == "__main__":
    main()