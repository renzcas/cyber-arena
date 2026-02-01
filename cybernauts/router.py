from flask import Blueprint, render_template, request, jsonify
from .prime import PrimeCybernaut
from .profiles import get_profile
from core.arena_state import get_arena_state

cybernauts_bp = Blueprint(
    "cybernauts",
    __name__,
    template_folder="../templates/cybernauts"
)

prime = PrimeCybernaut()

@cybernauts_bp.route("/")
def cockpit():
    return render_template("cybernauts/cockpit.html")

@cybernauts_bp.route("/think", methods=["POST"])
def think():
    profile_name = request.form.get("profile", "prime")
    message = request.form.get("message", "")

    profile = get_profile(profile_name)
    response = prime.process(message, profile)

    return render_template(
        "cybernauts/cockpit.html",
        profile_used=profile_name,
        user_message=message,
        cybernaut_response=response
    )
