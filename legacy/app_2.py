from flask import Flask, jsonify
from cybernauts.router import cybernauts_bp
from core.orchestrator import ArenaOrchestrator
from core.arena_state import get_arena_state, bind_orchestrator

app = Flask(__name__)

# Register the Cybernaut cockpit blueprint
app.register_blueprint(cybernauts_bp, url_prefix="/cybernauts")

# Instantiate orchestrator
orchestrator = ArenaOrchestrator(tick_rate=0.1)
bind_orchestrator(orchestrator)

# Start orchestrator when the server boots
@app.before_first_request
def start_orchestrator():
    orchestrator.start()

# Arena State API endpoint (now live)
@app.route("/api/arena/state")
def arena_state():
    return jsonify(orchestrator.get_state())

# Root route (optional)
@app.route("/")
def home():
    return "Cyber Arena Backend Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
