import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv

def main():
    env = GalaxyEnv(render_mode=None) # no rendering for training
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=100_000)
    model.save("ppo_galaxy_model")

if __name__ == "__main__":
    main()