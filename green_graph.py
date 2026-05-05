#!/usr/bin/env python3
"""
Green Graph Generator - Auto-commit tool to keep GitHub contribution graph green.
Creates daily commits automatically via cron job.
"""

import subprocess
import os
import random
from datetime import datetime

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(REPO_DIR, "activity.log")

def make_commit():
    os.chdir(REPO_DIR)
    
    now = datetime.now()
    messages = [
        f"refactor: code cleanup - {now.strftime('%Y-%m-%d')}",
        f"chore: update configs - {now.strftime('%Y-%m-%d')}",
        f"docs: improve documentation - {now.strftime('%Y-%m-%d')}",
        f"fix: minor bug fixes - {now.strftime('%Y-%m-%d')}",
        f"feat: optimize performance - {now.strftime('%Y-%m-%d')}",
        f"style: formatting improvements - {now.strftime('%Y-%m-%d')}",
        f"test: update test coverage - {now.strftime('%Y-%m-%d')}",
    ]
    
    # Write to log file
    with open(LOG_FILE, "a") as f:
        f.write(f"[{now.isoformat()}] Daily activity logged\n")
    
    # Git operations
    commit_msg = random.choice(messages)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    
    print(f"✅ Committed: {commit_msg}")

if __name__ == "__main__":
    try:
        make_commit()
    except Exception as e:
        print(f"❌ Error: {e}")
