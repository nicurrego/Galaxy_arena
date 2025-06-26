# Galaxy Arena — Personal Exploration Project

Welcome to my cosmic laboratory: an evolving reinforcement learning environment built to explore, experiment, and document my journey into agent intelligence. Here I teach spaceships how to survive and outsmart each other in digital combat.

---

## 🌌 Project Purpose

This repository is a **personal playground** to:

* Experiment with RL algorithms (PPO, later NEAT and more)
* Build agents that learn through trial, error, and clever reward shaping
* Document the triumphs, pitfalls, and incremental improvements of each phase
* Reflect on the evolution of my own understanding as much as the agents themselves

Every experiment is logged, every odd result a potential lesson. The journey is the product.

---

## 🚧 Contents & Structure

**Here’s how the project is organized:**

```
Galaxy_arena/
├── assets/             # Game images and sounds
├── core/               # Core game logic (spaceships, bullets, actions, constants)
├── envs/               # Custom Gymnasium environments (baseline, self-play, etc.)
├── logs/               # "Space Junk" logs & experiment results (csv, md)
├── models/             # Saved PPO models and experiment checkpoints
├── scripts/            # Training, evaluation, and manual play scripts
├── utils/              # Utilities (logging, helpers, etc.)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

* **core/**: Fundamental objects, rules, and constants for the game world.
* **envs/**: Reinforcement learning environments (each a different “lab” for experiments).
* **scripts/**: Training, evaluation, and manual play scripts.
* **models/**: Saved neural network weights—time capsules of agent minds.
* **logs/**: All experiment results and the developer’s diary.
* **assets/**: Visuals and sounds to bring the void to life.
* **utils/**: Logging tools and helpers to keep experiments organized.

---

## 📖 How to Read the Logs (`logs/`)

* **`experiment_results.csv`** — Raw log of experiments: each row is a snapshot of a training run (model, episodes, rewards, notes, etc.). Use this file to quickly scan results or analyze performance over time.
* **`exp_records.md`** — More detailed logs for experiments I consider interesting, with explanations, analysis, and lessons from particular runs. These are technical, not emotional.
* **`captains_log.md`** — This is my true developer’s diary—the emotional heart of the project. Each entry is a personal reflection: context, thoughts, struggles, mindset, and growth as I explore RL. This is not just about code, but my journey and perspective.

---

## 🪐 Final Note

This is not a polished product—just a chronicle of exploration and growth.
May it serve as a map of my galaxy and a beacon for the next journey.
