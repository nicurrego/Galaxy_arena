import gymnasium as gym
from stable_baselines3 import PPO
from envs.galaxy_env import GalaxyEnv

def main():
    env = GalaxyEnv(render_mode="human")
    model = PPO.load("ppo_galaxy_model")
    obs, _ = env.reset()
    done = False

    while not done:
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            done = True
        env.render()

    env.close()

if __name__ == "__main__":
    main()