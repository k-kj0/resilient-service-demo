"""
Watchdog script — simulates production restart behavior.
Run this alongside app.py to demo auto-recovery.
"""
import subprocess
import time
import sys

MAX_RESTARTS = 5
restart_count = 0

def start_server():
    return subprocess.Popen([sys.executable, "app.py"])

print("[watchdog] Starting service...")
proc = start_server()

while True:
    time.sleep(5)
    if proc.poll() is not None:  # process has exited
        restart_count += 1
        if restart_count > MAX_RESTARTS:
            print(f"[watchdog] Too many restarts ({restart_count}). Giving up.")
            break
        print(f"[watchdog] Service crashed! Restart #{restart_count}...")
        proc = start_server()
    else:
        print(f"[watchdog] Service healthy. Uptime check OK. (restarts: {restart_count})")
