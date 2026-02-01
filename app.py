from flask import Flask, jsonify
from cybernauts.router import cybernauts_bp
from core.arena_state import get_arena_state

app = Flask(__name__)

# Register the Cybernaut cockpit blueprint
app.register_blueprint(cybernauts_bp, url_prefix="/cybernauts")

# Arena State API endpoint
@app.route("/api/arena/state")
def arena_state():
    return jsonify(get_arena_state())

# Root route (optional)
@app.route("/")
def home():
    return "Cyber Arena Backend Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
