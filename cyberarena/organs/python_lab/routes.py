from flask import Blueprint, render_template, session
from .curriculum import COURSE_OUTLINE, LESSONS, LABS

python_lab_bp = Blueprint(
    "python_lab",
    __name__,
    template_folder="templates"
)

# -----------------------------
# Progress helper
# -----------------------------
def get_progress():
    return session.get("python_progress", [])


# -----------------------------
# Dashboard
# -----------------------------
@python_lab_bp.route("/python-lab")
def dashboard():
    return render_template(
        "python_lab/dashboard.html",
        outline=COURSE_OUTLINE,
        labs=LABS,
        progress=get_progress()
    )


# -----------------------------
# Lesson Page
# -----------------------------
@python_lab_bp.route("/python-lab/lesson/<lesson_id>")
def lesson(lesson_id):
    lesson = LESSONS.get(lesson_id)

    # Build list of lesson IDs
    ids = [item["id"] for item in COURSE_OUTLINE]
    current_index = ids.index(lesson_id)

    # Determine next lesson
    next_lesson = None
    if current_index < len(ids) - 1:
        next_lesson = ids[current_index + 1]

    return render_template(
        "python_lab/lesson.html",
        lesson=lesson,
        outline=COURSE_OUTLINE,
        next_lesson=next_lesson,
        lesson_id=lesson_id,
        progress=get_progress()
    )


# -----------------------------
# Mark Lesson Complete
# -----------------------------
@python_lab_bp.route("/python-lab/complete/<lesson_id>")
def complete_lesson(lesson_id):
    progress = session.get("python_progress", [])

    if lesson_id not in progress:
        progress.append(lesson_id)

    session["python_progress"] = progress
    return {"status": "ok", "progress": progress}


# -----------------------------
# Lab Page
# -----------------------------
@python_lab_bp.route("/python-lab/lab/<lab_id>")
def lab(lab_id):
    lab = LABS.get(lab_id)
    return render_template("python_lab/lab.html", lab=lab)


# -----------------------------
# Cybernaut Tutor API
# -----------------------------
@python_lab_bp.route("/python-lab/tutor/<lesson_id>/<action>")
def tutor(lesson_id, action):
    lesson = LESSONS.get(lesson_id)

    if not lesson:
        return {"response": "Lesson not found."}

    if action == "explain":
        response = (
            f"Here is a simple explanation of {lesson['title']}: "
            f"This lesson covers the following topics: {', '.join(lesson['topics'])}."
        )

    elif action == "example":
        example = lesson["examples"][0] if lesson["examples"] else "No examples available."
        response = f"Here is an example from this lesson:\n\n{example}"

    elif action == "quiz":
        topic = lesson["topics"][0]
        response = f"Quick quiz: Explain what '{topic}' means in your own words."

    else:
        response = "Unknown tutor action."

    return {"response": response}

@python_lab_bp.route("/python-lab/final-project")
def final_project():
    # Simple deterministic generator for now
    project = {
        "title": "Python Web App — Task Tracker",
        "description": (
            "Build a small Flask web application that lets users create, "
            "view, and delete tasks. Use templates, forms, and persistent storage."
        ),
        "features": [
            "Add new tasks",
            "List all tasks",
            "Delete tasks",
            "Store tasks in a JSON file or SQLite database",
            "Use templates with Jinja2",
        ],
        "structure": [
            "project/",
            "  app.py",
            "  templates/",
            "    index.html",
            "  static/",
            "    styles.css",
            "  data/",
            "    tasks.json",
        ],
        "starter_code": """from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO: load tasks, handle form submission, save tasks
    return render_template('index.html', tasks=[])

if __name__ == '__main__':
    app.run(debug=True)
""",
        "stretch_goals": [
            "Add user authentication",
            "Add categories or tags",
            "Add due dates",
            "Add a progress bar",
            "Deploy the app to a hosting platform",
        ],
    }

    return render_template(
        "python_lab/final_project.html",
        project=project
    )
