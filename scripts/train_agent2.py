import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env2 import GalaxyEnv2
from stable_baselines3.common.callbacks import CheckpointCallback
import os

algorithm = 'ppo'
model_name = 'X_'
model_number = '01'

checkpoint_callback = CheckpointCallback(
    save_freq=500_000,
    save_path="./models/",
    name_prefix=algorithm + '_' + model_name + '_' + model_number,
)

def main():
    # Optionally, set a model for the red ship (or None for random/scripted)
    red_ship_model_path = None

    # Create the multi-agent environment
    env = GalaxyEnv2(render_mode=None, red_ship_model_path=red_ship_model_path)

    # Wrap the env to only return yellow_ship's observation and reward for SB3
    class YellowShipWrapper(gym.Wrapper):
        def reset(self, **kwargs):
            obs_tuple, info = self.env.reset(**kwargs)
            return obs_tuple[0], info  # Only yellow_ship's obs

        def step(self, action):
            (obs, _), (yellow_reward, _), terminated, truncated, info = self.env.step(action, self.env.action_space.sample())
            return obs, yellow_reward, terminated, truncated, info

    wrapped_env = YellowShipWrapper(env)

    existing_model_path = "none"
    if os.path.exists(existing_model_path):
        print(f"Loading existing model from {existing_model_path}")
        model = PPO.load(existing_model_path, env=wrapped_env, verbose=1)
    else:
        print("Starting new model training")
        model = PPO("MlpPolicy", wrapped_env, verbose=1)

    print("Training yellow ship agent (red ship uses random actions)")
    model.learn(
        total_timesteps=300_000,
        callback=checkpoint_callback,
        reset_num_timesteps=False
    )

    # Save the final model
    model.save("./models/" + model_name + '_' + model_number)
    print("Training complete!")

if __name__ == "__main__":
    main()