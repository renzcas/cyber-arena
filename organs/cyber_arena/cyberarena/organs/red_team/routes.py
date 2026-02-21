from flask import Blueprint, render_template, request
from .recon import simulated_recon_scan
from .fuzzing import generate_fuzz_payloads
from .ai_attacks import simulate_ai_attack

red_team_bp = Blueprint(
    "red_team",
    __name__,
    template_folder="../../templates/red_team"
)

@red_team_bp.route("/")
def dashboard():
    return render_template("red_team/dashboard.html")

@red_team_bp.route("/recon", methods=["POST"])
def recon():
    target = request.form.get("target", "")
    results = simulated_recon_scan(target)
    return render_template("red_team/dashboard.html", recon_results=results)

@red_team_bp.route("/fuzz", methods=["POST"])
def fuzz():
    seed = request.form.get("seed", "")
    count = int(request.form.get("count", 10))
    payloads = generate_fuzz_payloads(seed, count)
    return render_template("red_team/dashboard.html", fuzz_results=payloads)

@red_team_bp.route("/ai_attack", methods=["POST"])
def ai_attack():
    vector = request.form.get("vector", "")
    result = simulate_ai_attack(vector)
    return render_template("red_team/dashboard.html", ai_results=result)

latest_red_events = []

def emit_red_event(event):
    latest_red_events.append(event)
    if len(latest_red_events) > 10:
        latest_red_events.pop(0)

def get_latest_red_events():
    return latest_red_events
