
---
**🚀 Model:** .\models\ppo_galaxy_model_100000_steps.zip

- **Date:** 2025-06-20 00:00:52
- **Episodes:** 5
- **Mean Reward:** 967.88
- **Std:** 1026.68
- **Min:** 21.00
- **Max:** 2336.30
- **Rewards:** 21.60;2336.30;373.50;2087.00;21.00
- **Notes:** The agent keeps going down and is being rewarded too much for surviving, which gives it the opposite of a winner's mindset.
Testing promotion.


---
**🚀 Model:** .\models\ppo_galaxy_model_survival_penalty_100000_steps.zip

- **Date:** 2025-06-20 10:02:00
- **Episodes:** 5
- **Mean Reward:** -6.68
- **Std:** 8.80
- **Min:** -11.08
- **Max:** 10.91
- **Rewards:** -11.08;10.91;-11.08;-11.07;-11.08
- **Notes:** Agent trained with survival penalty of -0.001.
The agent’s behavior changed dramatically with the survival penalty—no more lazy drifting! It’s now more focused on combat, showing early signs of learning, though it’s still a long way from ace pilot status.


---
**🚀 Model:** models/ppo_invincible_agent_final.zip

- **Date:** 2025-06-23 16:15:26
- **Episodes:** 5
- **Mean Reward:** 8.69
- **Std:** 6.20
- **Min:** 1.05
- **Max:** 13.85
- **Rewards:** 13.60;13.85;1.05;13.80;1.16
- **Notes:** Invincible agent evaluation.
The agent shows more attacking activity, lowing the penalty for being hitted elevates the chances to see less dodging and more combat.


---
**🚀 Model:** models\ppo_red_ship_Y-axis_movement.zip

- **Date:** 2025-06-23 17:00:20
- **Episodes:** 15
- **Mean Reward:** 13.45
- **Std:** 0.12
- **Min:** 13.20
- **Max:** 13.60
- **Rewards:** 13.46;13.49;13.53;13.60;13.60;13.49;13.46;13.56;13.32;13.43;13.35;13.24;13.52;13.20;13.45
- **Notes:** Evaluation of the agent with implementation of red ship y-axis movement II.
The agent shows a movement pattern that indicates is not trying to hide, but still can't say it has the purpose of dodging the red bullets, also it is fireing randomly.


---
**🚀 Model:** models\ppo_enhanced_red_ship.zip

- **Date:** 2025-06-23 17:27:17
- **Episodes:** 15
- **Mean Reward:** 13.56
- **Std:** 0.11
- **Min:** 13.33
- **Max:** 13.72
- **Rewards:** 13.43;13.54;13.44;13.44;13.33;13.54;13.64;13.64;13.51;13.64;13.64;13.64;13.72;13.64;13.65
- **Notes:** Evaluation of the agent with enhanced red ship behavior.
The agent doesn't care being shooted, it wins all the time though.

