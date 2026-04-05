# Resilient Service Demo
**MLH Production Engineering Hackathon — Reliability Category**

A production-ready service demonstrating health checks, crash simulation, and live monitoring.

## Live Demo
[View Dashboard](https://your-vercel-url.vercel.app)

## Endpoints
- `GET /` — Live status dashboard
- `GET /api/health` — JSON health check (uptime, status, timestamp)
- `GET /api/crash` — Simulates a crash and logs the incident

## Concepts demonstrated
- Health check / liveness probe pattern
- Incident logging and observability
- Auto-refresh monitoring dashboard
- Serverless resilient architecture

## Stack
Python (Vercel serverless) · Vanilla JS · HTML/CSS
