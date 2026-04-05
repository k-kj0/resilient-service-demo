import time
import threading
from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)
START_TIME = time.time()
restart_count = 0
incident_log = []

def get_uptime():
    return round(time.time() - START_TIME, 2)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "uptime_seconds": get_uptime(),
        "restarts": restart_count,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": "resilient-demo"
    })

@app.route("/crash")
def crash():
    """Simulate a crash for demo purposes"""
    incident_log.append({
        "time": datetime.now(timezone.utc).isoformat(),
        "event": "simulated crash triggered"
    })
    # In a real service, this would kill the process.
    # Here we just log it and return, showing the watchdog concept.
    return jsonify({"message": "Crash simulated and logged", "incidents": incident_log})

@app.route("/incidents")
def incidents():
    return jsonify({"incidents": incident_log, "total": len(incident_log)})

@app.route("/")
def dashboard():
    return open("dashboard.html").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
