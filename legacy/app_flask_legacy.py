from flask import Flask, jsonify, request
from flask_sock import Sock

from cybernauts.router import cybernauts_bp
from core.orchestrator import ArenaOrchestrator
from core.arena_state import get_arena_state, bind_orchestrator

app = Flask(__name__)
sock = Sock(app)

# Register cockpit blueprint
app.register_blueprint(cybernauts_bp, url_prefix="/cybernauts")

# Instantiate orchestrator
orchestrator = ArenaOrchestrator(tick_rate=0.1)

# Bind orchestrator to arena_state module
bind_orchestrator(orchestrator)

# ⭐ Start orchestrator immediately (Flask 3.x compatible)
orchestrator.start()

# Arena State API
@app.route("/api/arena/state")
def arena_state():
    return jsonify(get_arena_state())

# WebSocket Telemetry
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

# Console Command API
@app.route("/api/console/command", methods=["POST"])
def console_command():
    data = request.get_json(force=True) or {}
    channel = data.get("channel", "system")
    command = data.get("command", {})
    orchestrator.submit_command(channel, command)
    return jsonify({"status": "accepted", "channel": channel}), 202

@app.route("/")
def home():
    return "Cyber Arena Backend Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
