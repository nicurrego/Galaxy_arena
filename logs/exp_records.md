
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


---
**🚀 Model:** models\ppo_delayed_persecution.zip

- **Date:** 2025-06-23 18:39:15
- **Episodes:** 15
- **Mean Reward:** 12.34
- **Std:** 6.22
- **Min:** -10.91
- **Max:** 14.08
- **Rewards:** 14.07;14.07;14.06;14.07;14.06;14.08;13.09;14.06;14.08;-10.91;14.08;14.06;14.06;14.06;14.06
- **Notes:** New state, delayed persecution agent evaluation.
The agent shows splendid logic to win the battles, not perfect but very good performance. Lets not forget the bad skills the red ships got.


---
**🚀 Model:** models\ppo_first_trained_enemy.zip

- **Date:** 2025-06-24 00:04:05
- **Episodes:** 15
- **Mean Reward:** -11.14
- **Std:** 0.77
- **Min:** -11.90
- **Max:** -9.85
- **Rewards:** -11.87;-10.90;-10.87;-11.86;-9.85;-11.90;-11.88;-10.91;-10.88;-11.87;-9.90;-9.88;-11.87;-11.82;-10.81
- **Notes:** The enemy is the last trained agent.
The agent seems to like dodging the bullets, not quite skilled though. It seems like is not too interested in shooting.


---
**🚀 Model:** ./models/ppo_rewarded_hits.zip

- **Date:** 2025-06-24 00:21:28
- **Episodes:** 15
- **Mean Reward:** -11.91
- **Std:** 0.00
- **Min:** -11.91
- **Max:** -11.90
- **Rewards:** -11.91;-11.91;-11.91;-11.91;-11.91;-11.91;-11.91;-11.91;-11.91;-11.91;-11.90;-11.90;-11.91;-11.91;-11.91
- **Notes:** The enemy is the last trained agent and rewarder for hitting red ship.
The agent doesn't seems to be interested in shooting yet


---
**🚀 Model:** ./models/ppo_rewarded_hits_1M.zip

- **Date:** 2025-06-24 00:39:21
- **Episodes:** 15
- **Mean Reward:** -11.90
- **Std:** 0.04
- **Min:** -11.94
- **Max:** -11.84
- **Rewards:** -11.84;-11.94;-11.85;-11.94;-11.91;-11.87;-11.90;-11.94;-11.94;-11.90;-11.87;-11.94;-11.94;-11.87;-11.84
- **Notes:** The enemy is the last trained agent and rewarder for hitting red ship II.
The agent is afraid of dying, xd. The reward system needs to change!


---
**🚀 Model:** ./models/V1.zip

- **Date:** 2025-06-24 01:47:38
- **Episodes:** 15
- **Mean Reward:** 28.04
- **Std:** 0.00
- **Min:** 28.04
- **Max:** 28.04
- **Rewards:** 28.04;28.04;28.04;28.04;28.04;28.04;28.04;28.04;28.04;28.04;28.04;28.04;28.04;28.04;28.04
- **Notes:** V1 evaluation.
Agent wins all the time, it is due to the environment, lets see how it performs against itself


---
**🚀 Model:** ./models/V2.zip

- **Date:** 2025-06-24 15:08:07
- **Episodes:** 15
- **Mean Reward:** -1.97
- **Std:** 0.00
- **Min:** -1.97
- **Max:** -1.97
- **Rewards:** -1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97;-1.97
- **Notes:** V2 evaluation.
The model is failing in shooting the redship


---
**🚀 Model:** models\V8.zip

- **Date:** 2025-06-25 11:21:11
- **Episodes:** 10
- **Mean Reward:** -25.09
- **Std:** 0.00
- **Min:** -25.10
- **Max:** -25.09
- **Rewards:** -25.09;-25.10;-25.09;-25.10;-25.09;-25.09;-25.10;-25.09;-25.09;-25.09
- **Notes:** Agent goes down all the time and no more
after some trainings I've got to the conclution that I need to completely redo the reward system and check the agents build to improve performance


---
**🚀 Model:** models\Testing_02.zip

- **Date:** 2025-06-25 22:50:01
- **Episodes:** 10
- **Mean Reward:** 38.77
- **Std:** 12.93
- **Min:** 0.00
- **Max:** 43.80
- **Rewards:** 43.00;43.80;42.90;42.30;42.90;0.00;43.30;43.30;42.50;43.70
- **Notes:** The agent shoots but doesn't move, winning almost all the time
with this trained model I discovered that the reward system can change too much the performance of the agent, I believed I had a bug on the project but it was only the reward logic.


---
**🚀 Model:** models/A_03.zip

- **Date:** 2025-06-26 00:25:47
- **Episodes:** 10
- **Mean Reward:** -4.10
- **Std:** 3.31
- **Min:** -7.93
- **Max:** 4.26
- **Rewards:** -3.73;-3.56;-7.59;-3.54;-7.52;-3.77;-3.61;-7.93;-3.98;4.26
- **Notes:** The agent goes forward, shoots too few bullets, not capable of winning
Rewards:  
```
reward = -0.01  # step penalty to discourage stalling

        if red_was_hit:
            reward += 4.0
        if yellow_was_hit:
            reward -= 1.0
        if self.red_health <= 0:
            reward += 10.0  # win
        if self.yellow_health <= 0:
            reward -= 3.0  # loss
```


---
**🚀 Model:** models/A_04.zip

- **Date:** 2025-06-26 00:58:54
- **Episodes:** 10
- **Mean Reward:** 49.33
- **Std:** 0.29
- **Min:** 48.45
- **Max:** 49.45
- **Rewards:** 48.45;49.42;49.43;49.43;49.43;49.42;49.45;49.42;49.43;49.44
- **Notes:** the agent learned to win always by only shooting 'cause the red ship goes rigth into the bullets when starting the battle
Rewards:
```
reward = -0.01  # step penalty to discourage stalling

        if red_was_hit:
            reward += 10.0
        if yellow_was_hit:
            reward -= 1.0
        if self.red_health <= 0:
            reward += 10.0  # win
        if self.yellow_health <= 0:
            reward -= 3.0  # loss

        return reward
```
- Against human:
**The agent doesn't move at all**

---
**🚀 Model:** models/B_01.zip

- **Date:** 2025-06-26 09:40:34
- **Episodes:** 10
- **Mean Reward:** 0.00
- **Std:** 1.00
- **Min:** -1.00
- **Max:** 1.00
- **Rewards:** -1.00;1.00;1.00;-1.00;1.00;1.00;-1.00;-1.00;1.00;-1.00
- **Notes:** The agent avoids dying at the start but don't quite understand the concept of dodging bullets, also it fires and hits on the enemy that runs towards the yellow ship.
Rewards:
```
reward = 0.0  # step penalty to discourage stalling

        if red_was_hit:
            reward += 0.0
        if yellow_was_hit:
            reward -= 0.0
        if self.red_health <= 0:
            reward += 1.0  # win
        if self.yellow_health <= 0:
            reward -= 1.0  # loss
```
- Against human:
**The agent goes backwards and fires randomly**

---
**🚀 Model:** models/B_02.zip

- **Date:** 2025-06-26 09:51:25
- **Episodes:** 10
- **Mean Reward:** 2.50
- **Std:** 0.67
- **Min:** 1.00
- **Max:** 3.00
- **Rewards:** 3.00;3.00;2.00;3.00;3.00;3.00;1.00;3.00;2.00;2.00
- **Notes:** Very nice performance so far.
Rewards:
```
 reward = 0.0  # step penalty to discourage stalling

        if red_was_hit:
            reward += 1.0
        if yellow_was_hit:
            reward -= 1.0
        if self.red_health <= 0:
            reward += 0.0  # win
        if self.yellow_health <= 0:
            reward -= 0.0  # loss
```
- Against human:
**The agent tries to fire but it seems too scare to seek front combat**


---
**🚀 Model:** models/B_03.zip

- **Date:** 2025-06-26 10:01:13
- **Episodes:** 10
- **Mean Reward:** -1.80
- **Std:** 0.66
- **Min:** -3.70
- **Max:** -1.30
- **Rewards:** -1.70;-1.50;-1.30;-1.60;-1.40;-1.80;-1.50;-3.70;-1.60;-1.90
- **Notes:** The agent learned to shoot and avoid at the very beggining and seems to win frequently.
Rewards:
```
 reward = -0.1  # step penalty to discourage stalling

        if red_was_hit:
            reward += 1.0
        if yellow_was_hit:
            reward -= 2.0
        if self.red_health <= 0:
            reward += 0.0  # win
        if self.yellow_health <= 0:
            reward -= 0.0  # loss
```
- Against human:
**Not really aiming to hit the enemy**
---
**🚀 Model:** models/B_04.zip

- **Date:** 2025-06-26 10:09:40
- **Episodes:** 10
- **Mean Reward:** -9.07
- **Std:** 1.74
- **Min:** -11.90
- **Max:** -6.20
- **Rewards:** -10.00;-9.20;-10.50;-6.20;-6.30;-9.40;-9.80;-9.80;-11.90;-7.60
- **Notes:** The agent doesn't show any particular objective on his performance.
Rewards:
```
reward = -0.1  # step penalty to discourage stalling

        if red_was_hit:
            reward += 2.0
        if yellow_was_hit:
            reward -= 1.0
        if self.red_health <= 0:
            reward += 0.0  # win
        if self.yellow_health <= 0:
            reward -= 0.0  # loss
```
- Against human:
**Not good**