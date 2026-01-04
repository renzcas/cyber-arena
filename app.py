from flask import Flask
from flask import session


# --- Organs ---
from organs.red_team.routes import red_team_bp
from organs.blue_team.routes import blue_team_bp
from organs.grey_team.routes import grey_team_bp
from organs.python_lab import python_lab_bp

# --- Cybernauts ---
from cybernauts.router import cybernauts_bp

# --- Math Engine ---
from math_engine.routes import math_engine_bp

from prime_cockpit.routes import prime_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(red_team_bp, url_prefix="/red")
app.register_blueprint(blue_team_bp, url_prefix="/blue")
app.register_blueprint(grey_team_bp, url_prefix="/grey")
app.register_blueprint(cybernauts_bp, url_prefix="/cybernauts")
app.register_blueprint(math_engine_bp, url_prefix="/math_engine")
app.register_blueprint(prime_bp, url_prefix="/prime")
app.register_blueprint(python_lab_bp)

app.secret_key = "super-secret-key"  # replace with env var later

@app.route("/")
def index():
    return """
    <h1>CyberArena</h1>
    <p>Welcome to the Arena. Enter the Prime Cockpit:</p>
    <ul>
        <li><a href='/prime'>Prime Cockpit</a></li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
