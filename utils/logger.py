import csv
from datetime import datetime

def log_to_csv(filepath, model, episodes, rewards, notes=""):
    mean_reward = sum(rewards) / len(rewards)
    min_reward = min(rewards)
    max_reward = max(rewards)
    std_reward = (sum([(r - mean_reward) ** 2 for r in rewards]) / len(rewards)) ** 0.5

    file_exist = False
    try:
        with open(filepath, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filepath, "a", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "model", "episodes", "mean", "std", "min", "max", "rewards", "notes"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            model,
            episodes,
            f"{mean_reward:.2f}",
            f"{std_reward:.2f}",
            f"{min_reward:.2f}",
            f"{max_reward:.2f}",
            ";".join([f"{r:.2f}" for r in rewards]),
            notes
        ])
        