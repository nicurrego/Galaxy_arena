
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

