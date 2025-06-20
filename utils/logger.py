import csv
from datetime import datetime
import os

def log_to_csv(filepath, model, episodes, rewards, notes=""):
    """
    Appends evaluation results to a CSV file, creating it with headers if it doesn't exist.
    The notes field is wrapped in double quotes, along with all other fields.
    """
    # Calculate statistics
    mean_reward = sum(rewards) / len(rewards)
    min_reward = min(rewards)
    max_reward = max(rewards)
    std_reward = (sum((r - mean_reward) ** 2 for r in rewards) / len(rewards)) ** 0.5

    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Check if file exists (to write header)
    write_header = not os.path.exists(filepath)

    # Open CSV for appending, quoting all fields with double quotes
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, quotechar='"')
        if write_header:
            writer.writerow([
                "date", "model", "episodes",
                "mean", "std", "min", "max",
                "rewards", "notes"
            ])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            model,
            episodes,
            f"{mean_reward:.2f}",
            f"{std_reward:.2f}",
            f"{min_reward:.2f}",
            f"{max_reward:.2f}",
            ";".join(f"{r:.2f}" for r in rewards),
            notes  # quotes handled by csv.QUOTE_ALL
        ])

def log_to_md(filepath, model, episodes, rewards, notes=""):
    mean_reward = sum(rewards) / len(rewards)
    min_reward = min(rewards)
    max_reward = max(rewards)
    std_reward = (sum([(r - mean_reward) ** 2 for r in rewards]) / len(rewards)) ** 0.5

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"\n---\n")
        f.write(f"**Model:** {model}\n\n")
        f.write(f"- **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"- **Episodes:** {episodes}\n")
        f.write(f"- **Mean Reward:** {mean_reward:.2f}\n")
        f.write(f"- **Std:** {std_reward:.2f}\n")
        f.write(f"- **Min:** {min_reward:.2f}\n")
        f.write(f"- **Max:** {max_reward:.2f}\n")
        f.write(f"- **Rewards:** {', '.join([f'{r:.2f}' for r in rewards])}\n")
        if notes:
            f.write(f"- **Notes:** {notes}\n")

def promote_csv_to_md(csv_path, md_path, row_idx=-1, extra_notes=None):
    # row_idx=-1: last row; or pass any integer for previous runs
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        headers, *rows = reader
        if not rows:
            print("No runs to promote.")
            return
        row = rows[row_idx]

    # Extract all values
    log = dict(zip(headers, row))
    notes = log.get("notes", "")
    if extra_notes:
        notes = f"{notes}\n{extra_notes}" if notes else extra_notes

    # Write to MD in your desired format
    with open(md_path, "a", encoding="utf-8") as f:
        f.write(f"\n---\n")
        f.write(f"**🚀 Model:** {log['model']}\n\n")
        f.write(f"- **Date:** {log['date']}\n")
        f.write(f"- **Episodes:** {log['episodes']}\n")
        f.write(f"- **Mean Reward:** {log['mean']}\n")
        f.write(f"- **Std:** {log['std']}\n")
        f.write(f"- **Min:** {log['min']}\n")
        f.write(f"- **Max:** {log['max']}\n")
        f.write(f"- **Rewards:** {log['rewards']}\n")
        if notes:
            f.write(f"- **Notes:** {notes}\n")
        f.write("\n")
# Usage:
# promote_csv_to_md("logs/experiment_results.csv", "logs/experiment_results.md", extra_notes="Agent learned to dodge for the first time! 🎉")