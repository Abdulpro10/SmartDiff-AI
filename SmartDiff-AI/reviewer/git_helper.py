import subprocess
import sys

def get_staged_diff():
    try:
        result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception:
        return None

def is_git_repository():
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True, check=True)
        return True
    except Exception:
        return False