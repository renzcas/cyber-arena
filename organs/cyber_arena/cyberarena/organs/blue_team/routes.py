from flask import Blueprint, render_template, request
from .log_analysis import simulate_log_analysis
from .anomaly_detection import detect_anomalies
from .zero_trust import evaluate_zero_trust
from .deception import generate_deception_events

blue_team_bp = Blueprint(
    "blue_team",
    __name__,
    template_folder="../../templates/blue_team"
)

@blue_team_bp.route("/")
def dashboard():
    return render_template("blue_team/dashboard.html")

@blue_team_bp.route("/logs", methods=["POST"])
def logs():
    sample = request.form.get("sample", "")
    results = simulate_log_analysis(sample)
    return render_template("blue_team/dashboard.html", log_results=results)

@blue_team_bp.route("/anomaly", methods=["POST"])
def anomaly():
    data = request.form.get("data", "")
    results = detect_anomalies(data)
    return render_template("blue_team/dashboard.html", anomaly_results=results)

@blue_team_bp.route("/zero_trust", methods=["POST"])
def zero_trust():
    identity = request.form.get("identity", "")
    score = evaluate_zero_trust(identity)
    return render_template("blue_team/dashboard.html", zero_trust_score=score)

@blue_team_bp.route("/deception", methods=["POST"])
def deception():
    count = int(request.form.get("count", 5))
    events = generate_deception_events(count)
    return render_template("blue_team/dashboard.html", deception_events=events)

latest_blue_events = []

def emit_blue_event(event):
    latest_blue_events.append(event)
    if len(latest_blue_events) > 10:
        latest_blue_events.pop(0)

def get_latest_blue_events():
    return latest_blue_events
