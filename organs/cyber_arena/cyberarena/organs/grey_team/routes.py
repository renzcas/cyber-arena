from flask import Blueprint, render_template, request
from .web_bots import simulate_web_bot
from .recon_bots import automated_recon
from .automation import run_automation_task

grey_team_bp = Blueprint(
    "grey_team",
    __name__,
    template_folder="../../templates/grey_team"
)

@grey_team_bp.route("/")
def dashboard():
    return render_template("grey_team/dashboard.html")

@grey_team_bp.route("/web_bot", methods=["POST"])
def web_bot():
    url = request.form.get("url", "")
    result = simulate_web_bot(url)
    return render_template("grey_team/dashboard.html", web_bot_result=result)

@grey_team_bp.route("/recon_bot", methods=["POST"])
def recon_bot():
    target = request.form.get("target", "")
    results = automated_recon(target)
    return render_template("grey_team/dashboard.html", recon_bot_results=results)

@grey_team_bp.route("/automation", methods=["POST"])
def automation():
    task = request.form.get("task", "")
    output = run_automation_task(task)
    return render_template("grey_team/dashboard.html", automation_output=output)


latest_grey_events = []

def emit_grey_event(event):
    latest_grey_events.append(event)
    if len(latest_grey_events) > 10:
        latest_grey_events.pop(0)

def get_latest_grey_events():
    return latest_grey_events
