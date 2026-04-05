from datetime import datetime, timezone
import time

START = time.time()
restarts = 0

def handler(request):
    from http.server import BaseHTTPRequestHandler
    pass

# Vercel serverless function
def handler(request):
    import json
    data = {
        "status": "healthy",
        "uptime_seconds": round(time.time() - START, 2),
        "restarts": restarts,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": "resilient-demo"
    }
    from flask import Response
    return Response(json.dumps(data), mimetype="application/json")
