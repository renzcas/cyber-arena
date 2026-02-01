from flask import Flask, jsonify, request
from flask_sock import Sock

from cybernauts.router import cybernauts_bp
from core.orchestrator import ArenaOrchestrator
from core.arena_state import get_arena_state, bind_orchestrator

app = Flask(__name__)
sock = Sock(app)

# Register the Cybernaut cockpit blueprint
app.register_blueprint(cybernauts_bp, url_prefix="/cybernauts")

# Instantiate orchestrator
orchestrator = ArenaOrchestrator(tick_rate=0.1)

# Bind orchestrator to arena_state module
bind_orchestrator(orchestrator)

# Start orchestrator when the server boots
@app.before_first_request
def start_orchestrator():
    orchestrator.start()

# Arena State API endpoint (live state)
@app.route("/api/arena/state")
def arena_state():
    return jsonify(get_arena_state())

# WebSocket Telemetry endpoint
@sock.route('/ws/arena')
def arena_ws(ws):
    orchestrator.telemetry.register(ws)
    try:
        while True:
            msg = ws.receive()
            if msg is None:
                break
    finally:
        orchestrator.telemetry.unregister(ws)

# Team Console command endpoint
@app.route("/api/console/command", methods=["POST"])
def console_command():
    data = request.get_json(force=True) or {}
    channel = data.get("channel", "system")
    command = data.get("command", {})

    orchestrator.submit_command(channel, command)

    return jsonify({"status": "accepted", "channel": channel}), 202

# Root route (optional)
@app.route("/")
def home():
    return "Cyber Arena Backend Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
