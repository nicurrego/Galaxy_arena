# Captain’s Log Index

Navigate the cosmic mess of development!  
Here’s your running table of contents for Space Junk entries:

- [Space Junk #001](#space-junk-001)
- [Space Junk #002](#space-junk-002)
- [Space Junk #003](#space-junk-003)
- [Space Junk #004](#space-junk-004)


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