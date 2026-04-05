from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timezone

incidents = []

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        incidents.append({
            "time": datetime.now(timezone.utc).isoformat(),
            "event": "simulated crash triggered"
        })
        data = {"message": "Crash simulated and logged", "total_incidents": len(incidents)}
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
