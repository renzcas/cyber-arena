from flask import Blueprint, render_template, request, jsonify
from .core import process_math
from .transform_engine import TransformEngine
import math

math_engine_bp = Blueprint(
    "math_engine",
    __name__,
    template_folder="../templates/math_engine"
)

@math_engine_bp.route("/")
def dashboard():
    return render_template("math_engine/dashboard.html")

@math_engine_bp.route("/compute", methods=["POST"])
def compute():
    query = request.form.get("query", "")
    result = process_math(query)
    return render_template("math_engine/dashboard.html", query=query, result=result)

# ---------------------------------------------------------
# NEW: Perspective–Zeta Duality endpoint
# ---------------------------------------------------------
@math_engine_bp.route("/perspective_zeta", methods=["POST"])
def perspective_zeta():
    data = request.json

    theta = float(data.get("theta", 0))
    px = float(data.get("px", 0))
    py = float(data.get("py", 0))
    pz = float(data.get("pz", 1))

    # Build transforms
    R = TransformEngine.rotation_y(theta)
    P = TransformEngine.perspective(px, py, pz)

    # Transform a default point (or user-provided)
    point = data.get("point", [1, 0, 0])
    rotated = R.apply(point)
    projected = P.apply(rotated)

    return jsonify({
        "rotated": rotated,
        "projected": projected
    })
