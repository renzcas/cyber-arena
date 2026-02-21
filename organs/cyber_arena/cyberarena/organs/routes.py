# python_lab/routes.py

from flask import Blueprint, render_template
from .curriculum import COURSE_OUTLINE, LESSONS, LABS

python_lab_bp = Blueprint(
    "python_lab",
    __name__,
    template_folder="templates"
)

@python_lab_bp.route("/python-lab")
def dashboard():
    return render_template("python_lab/dashboard.html", outline=COURSE_OUTLINE)

@python_lab_bp.route("/python-lab/lesson/<lesson_id>")
def lesson(lesson_id):
    lesson = LESSONS.get(lesson_id)
    return render_template("python_lab/lesson.html", lesson=lesson)

@python_lab_bp.route("/python-lab/lab/<lab_id>")
def lab(lab_id):
    lab = LABS.get(lab_id)
    return render_template("python_lab/lab.html", lab=lab)
