import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv
from stable_baselines3.common.callbacks import CheckpointCallback
import os

checkpoint_callback = CheckpointCallback(
    save_freq=250_000,
    save_path="./models/",
    name_prefix=''
)

def main():
    # Initialize two neural networks to play agains each other.