# Resilient Service Demo — MLH Production Engineering Hackathon

A production-grade reliability demo showing health checks, auto-restart, and live monitoring.

## What it does
- `/health` — JSON health endpoint with uptime & restart count
- `/crash` — Simulates a crash and logs the incident
- `/incidents` — Incident log
- `/` — Live status dashboard (auto-refreshes every 5s)
- `watchdog.py` — Auto-restarts the service if it crashes

## How to run (Replit — no install needed)
1. Fork this repo into [Replit](https://replit.com)
2. Click **Run**
3. Open the web preview — you'll see the live dashboard

## Reliability concepts demonstrated
- Health checks (liveness probe pattern)
- Auto-restart / watchdog process (like `--restart=always` in Docker)
- Incident logging and observability
- Zero-downtime design goal

## Tech stack
Python · Flask · Vanilla JS
