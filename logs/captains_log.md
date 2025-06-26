# Captain’s Log Index

Navigate the cosmic mess of development!  
## 🚀 Project Highlights

- [Space Junk #004](#space-junk-004) — First Agent Training Milestone  
- [Space Junk #012](#space-junk-012) — The Great Reward Revelation  
- [Space Junk #014](#space-junk-014) — New Frontier: Agent-vs-Agent & Evolution

---

## Space Junk Template

**Mission Time:** {date / timestamp}  
**Coordinates:** {stage of project / milestone}

#### 🚀 Context:
Summary of what you tried or built. Code, features, experiments, bugs, new approaches… whatever you were working on. Be concise or detailed—your call!

#### 🌌 Thoughts:
What did you learn, realize, or face? Unexpected bugs, breakthrough ideas, obstacles, or even emotional highs/lows—share it all!

#### 🛠️ Insights:
Key code changes, experiments run, or configuration tweaks. Screenshots or code snippets welcome.

#### 🧭 Next:
What’s next? Next action, open questions, or reflections about where you’ll go from here.

#### 🫠 Mood:
Share a meme-able moment or a one-liner about how you feel.



# Space Junk #001

**Coordinates:** Phase 1 – Project Foundation

#### 🚀 Context:
Launched the mission! Established the overall vision: to build a modular, gym-compatible RL environment inspired by classic spaceship duels. Started the project repo and directory layout. Core files for `constants.py`, `actions.py`, and `spaceship.py` created.


#### 🛠️ Insights:
- Defined constants for colors, screen, ship, etc.
- Laid out clear, modular folder structure (`core/`, `envs/`, `scripts/`).
- Committed to phase-based milestones for growth.

#### 🧭 Next:
Get *something* visible! Implement a basic `Spaceship` class and show the first pixel movement. Proof-of-life required.

# Space Junk #002

**Coordinates:** Phase 1 – Visual Feedback

#### 🚀 Context:
Spaceships appeared on the screen for the first time! Manual controls (WASD) enabled for a human pilot. Wrote `human_play.py` script for interactive testing.

#### 🛠️ Insights:
- Implemented the spaceship `draw()` and `move()` logic.
- Added user input loop for manual play.
- Project structure now supports flexible run scripts.

#### 🧭 Next:
Add interaction! Design bullet mechanics, enable firing, and build a collision system. RL without feedback is like a ship with no thrusters.

# Space Junk #003

**Coordinates:** Phase 2 – Bullets & Combat

#### 🚀 Context:
First taste of combat. Bullets, shooting delays, health points, and basic collision detection landed. Now the void shoots back!

#### 🛠️ Insights:
- Created `bullet.py` and bullet logic in ships.
- Implemented health tracking and rewards.
- Added per-frame update system for movement and collision.

#### 🧭 Next:
Begin simple agent logic and baseline AI. Make it possible for “the void” to fight back!

# Space Junk #004
**Mission Time:** 2025-06-19 11:15am  
**Coordinates:** Phase 3 – Agent Training

#### 🚀 Context:
Integrated PPO agent from Stable Baselines3. Model checkpointing and experiment tracking now online! Watched as the AI began to *almost* learn basic survival and combat. Human-level not yet, but stars are aligning.

Created logs module to the repo, to keep track of all the madness.

#### 🌌 Thoughts:
There’s so much I want to share, but what excites me the most is knowing these stories will live on through my work.  
About the agent: it moves! 😂 It doesn’t really have a sense of purpose yet, but when it manages to survive those first few seconds, it almost feels alive.


#### 🛠️ Insights:
- Added experiment log and checkpointing callbacks.
- Fixed obs shape mismatches and bugs.
- Evaluated model: agent dodges and shoots (sometimes!).

#### 🧭 Next:
Refine reward logic, implement more advanced agent logic, and document all the moving parts for future explorers.

#### 🥲✨ Mood:
So happy to se my hours of work kinda alife!

# Space Junk #005

**Mission Time:** 2025-06-19 10:28pm  
**Coordinates:** Phase 3 - Agent Training (logging)

#### 🚀 Context:
Attempted to roll out the shiny new logging utilities from the utils directory, eager to track my agent’s performance in experiment_results.csv. 


#### 🌌 Thoughts:
There’s something oddly satisfying about watching numbers appear in the log file… if only they actually did. Spent a good chunk of time marveling at my agent’s questionable life choices, and wondering, "Will this training ever end?" (Spoiler: Not today.)

#### 🛠️ Insights:
The agent gamely pressed on until the final reward, but it turns out all that time was for naught—my logging function had a bug and none of the results made it to the CSV.

#### 🧭 Next:
Fix the logging error and give it another go.

#### 😑 Mood:
Are you kidding me?.

# Space Junk #006

**Mission Time:** 2025-06-20 12:20am  
**Coordinates:** Phase 3 - Agent Training (logging II)

#### 🚀 Context:
Running the experiment again, this time with the logging function fixed.

#### 🌌 Thoughts:
The reward system is inefficient in this environment.
It’s curious how the agent tends to move downward often.
The notes parameter in the logger feels useless right now—maybe it would help if I left meaningful comments for reviewers, but for now I realize: I can’t comment on events I haven’t logged.

#### 🛠️ Insights:
It would be useful to track episode duration.
I want to link the CSV log info with the agent’s parameters and environment settings.

#### 🧭 Next:
How do I turn this agent into a gladiator who relentlessly seeks victory?

#### 🫠 Mood:
Smooth runs always leave room to breathe—sometimes it’s just hot air in endless training.

# Space Junk #007

**Mission Time:** 2025-06-23 12:22pm  
**Coordinates:** Phase 3 - Agent Training (Truncated)

#### 🚀 Context:
I needed to handle evaluations to make it bearable and avoid infinite dummy loops.

#### 🌌 Thoughts:
Why did the answer hide in plain sight, cloaked in the quiet folds of “truncated”?
Sometimes the mind must pause, rest, and let the stars align before truth can shine.

#### 🛠️ Insights:
I gained a better understanding of the Gymnasium API.
Resting clears the fog, revealing what was always there, just beyond tired eyes.

#### 🧭 Next:
Train a invinsible agent

#### 🫠 Mood:
Time slips through my fingers like cosmic dust—
I must finish this now, or be forever lost in the endless spiral of beginnings.

# Space Junk #008

**Mission Time:** 2025-06-23 06:00pm  
**Coordinates:** Phase 3 - Agent Training (Rendering)

#### 🚀 Context:  
After enhancing the red ship's behavior, I wanted to evaluate it.  
For that reason, I added a new file to handle rendering without modifying the original human_play.py file.

#### 🌌 Thoughts:  
The gameplay is very hard for a human; the movement has many bugs and the movement limitations are not well set,  
however, this can be a good feature for training an agent.

#### 🛠️ Insights:  
Need a refactor of the envs to make it more modular and easier to test.

#### 🧭 Next:  
Evaluate agent with new red ship behavior.

#### 🫠 Mood:  
Cleaning is a chore no one wants to do, but it is necessary to keep the ship afloat.

# Space Junk #009

**Mission Time:** 2025-06-23 06:41pm  
**Coordinates:** Phase 3 - Agent Training (Enemy AI)

#### 🚀 Context:  
Refactored the envs to make them more modular and easier to test.  
Trained a model with 500k steps that performed better than the previous one.  
- This agent has only 2 lives, which are more valuable than the previous 4 lives.  
- The red ship follows the yellow ship along the Y axis and tries to maintain distance on the X axis.  
- Both ships fire randomly.

#### 🌌 Thoughts:  
You don’t know what you have until you lose it! After being nerfed from 4 to 2 lives, the yellow ship shows more survival and attacking behavior.  
The better the environment, the better the training.

#### 🛠️ Insights:  
The ships behave better; however, the agent is still not able to learn the best strategy to win.

#### 🧭 Next:  
- Make the last trained agent the enemy.  

#### 🫠 Mood:  
My back hurts! I'm at school and trying to work on this project.

# Space Junk #010

**Mission Time:** 2025-06-24 03:44 PM  
**Coordinates:** Phase 3 - Agent Training ('V' models)

#### 🚀 Context:  
After training several models, I tried a different approach and now I’m naming the models 'V#' (# is the model number).

I found it interesting that the environment leads to very short combats; it’s too easy to lose or win since the only thing needed is to shoot and hit the enemy.

In some models, I managed to make them dodge but they wouldn’t fire, so they were survivors, not warriors.

In other models, I made them fire but not dodge, so they were kamikazes, not winners.

#### 🌌 Thoughts:  
- Changing the environment (e.g., starting positions of the ships so they don’t face each other from the beginning) will improve exploration.

#### 🛠️ Insights:  
The current model, V3, only dodges when bullets are fired but does not aim to hit the enemy.

#### 🧭 Next Steps:  
- Modify the environment to encourage better exploration.

#### 🧪 Mood:  
I feel just like a true scientist. 

# Space Junk #011

**Mission Time:** 2025-06-25 01:59 AM  
**Coordinates:** Phase 3 - Agent Training ('V' BUGS)

#### 🚀 Context:  
After training several models, I noticed all of them only move up or down with no other apparent behavior during evaluation runs. This indicates there is a bug that I need to find.

#### 🌌 Thoughts:  
- At some point, I must have changed something that broke the agents' training.
- However, model V5 performs pretty well compared to others, so I will check what conditions V5 was trained under to find the bug.

#### 🛠️ Insights:  
Models trained after V5 could have worked properly if the bug didn’t exist!

#### 🧭 Next Steps:  
- Fix the bug.

#### 🤯 Mood:  
A lot of work and thinking for this, really? 

# Space Junk #012

**Mission Time:** 2025-06-25 01:13 AM  
**Coordinates:** Phase 3 - Agent Training (REWARDS)

#### 🚀 Context:  
- I’ve been digging through past project versions, hunting for the source of this issue—and it’s exhausting!
- I’ve trained more “insightful” agents, but the red ship (the enemy in the environment) is still allowing lazy behaviors.

#### 🌌 Thoughts:  
- The best way to fix bugs is to prevent them in the first place.
- I need to document things better to keep track of the project’s evolution and avoid these energy-draining, soul-sapping debugging sessions.
- A better environment will breed better models.

#### 🛠️ Insights:  
The problem wasn’t in the code logic, but in the **reward system**.

#### 🧭 Next Steps:  
- Upgrade, modify, or do whatever’s necessary to improve training.
- Maybe it’s time for a better red ship AI?!

#### 🧠 Mood:  
Reading the same code over and over is a good cardio workout for the mind, XD.  
Honestly, it’s like running a marathon, a mental fight above all else!

# Space Junk #013

**Mission Time:** 2025-06-26 10:12 AM  
**Coordinates:** Phase 3 - Agent Training ('B' models)

#### 🚀 Context:  
- Tweaked the rewards only slightly and trained multiple models with ~3k timesteps each to observe performance changes. 

#### 🌌 Thoughts:  
- The agent, when trained against the baseline enemy, achieves its goal quite well—given enough timesteps and a logical reward system. 
- For multiplayer combat, what we need are *skills*, not just systems. 

#### 🛠️ Insights:  
- Each model achieves different performance, but all seem to follow the reward system as faithfully as devotees follow their gods. 

#### 🧭 Next Steps:  
- Build an environment where models can train against other training models, so both can evolve with each iteration. 

#### ☕🚶‍♂️✨ Mood:  
- Sleepy, but the road I’ve traveled keeps me going. 

# Space Junk #014

**Mission Time:** 2025-06-26 01:42 AM  
**Coordinates:** Phase 3 - Agent Training ('X' models)

#### 🚀 Context:  
- New environment for training agent vs agent.
- New training script.
- New trained model.

#### 🌌 Thoughts:  
- I was hoping for better results, but I realized the process I had in mind requires a different approach.

#### 🛠️ Insights:  
- With this new environment, I can only train one learning agent versus a random agent—not true dual-agent learning yet.

#### 🧭 Next Steps:  
- Close the project with a README.md and continue on my quest to master both NEAT and RL worlds.

#### 🥱🙏✨ Mood:  
- Still sleepy, but grateful for the chance to learn by doing!

