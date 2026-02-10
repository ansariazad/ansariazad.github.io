#!/usr/bin/env python3
"""
Green Graph Backfill — Fill GitHub contribution graph for past 90 days.
Creates backdated commits to show consistent activity.
Run ONCE only.
"""

import subprocess
import os
import random
from datetime import datetime, timedelta

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(REPO_DIR, "activity.log")

def backfill():
    os.chdir(REPO_DIR)
    today = datetime.now()
    
    for days_ago in range(90, 0, -1):
        date = today - timedelta(days=days_ago)
        
        # Skip some days randomly (looks more natural - 70% chance of commit)
        if random.random() > 0.72:
            continue
        
        # 1-3 commits per day
        num_commits = random.randint(1, 3)
        
        for c in range(num_commits):
            hour = random.randint(9, 22)
            minute = random.randint(0, 59)
            commit_date = date.replace(hour=hour, minute=minute)
            date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
            
            messages = [
                f"refactor: code improvements",
                f"chore: update dependencies",
                f"docs: update documentation",
                f"fix: resolve edge case",
                f"feat: add new feature",
                f"style: formatting cleanup",
                f"test: improve coverage",
                f"perf: optimize performance",
            ]
            
            # Write to log
            with open(LOG_FILE, "a") as f:
                f.write(f"[{date_str}] Activity logged (backfill)\n")
            
            msg = random.choice(messages)
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str
            
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", msg, "--allow-empty"], 
                         env=env, check=True, capture_output=True)
    
    # Push all commits
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("✅ Backfill complete! Green graph should update in a few minutes.")

if __name__ == "__main__":
    backfill()
