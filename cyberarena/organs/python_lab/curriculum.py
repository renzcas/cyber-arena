# organs/python_lab/curriculum.py

COURSE_OUTLINE = [
    {"id": "01", "title": "Python Basics"},
    {"id": "02", "title": "Control Flow"},
    {"id": "03", "title": "Functions"},
    {"id": "04", "title": "Data Structures"},
    {"id": "05", "title": "Modules & Packages"},
    {"id": "06", "title": "File I/O"},
    {"id": "07", "title": "Error Handling"},
    {"id": "08", "title": "Virtual Environments & pip"},
    {"id": "09", "title": "Working With APIs (requests)"},
    {"id": "10", "title": "JSON & Data Parsing"},
    {"id": "11", "title": "Intro to Flask"},
    {"id": "12", "title": "Flask Routing & Views"},
    {"id": "13", "title": "Templates & Jinja2"},
    {"id": "14", "title": "Forms & POST Requests"},
    {"id": "15", "title": "Databases With SQLite"},
    {"id": "16", "title": "ORM Basics (SQLAlchemy style)"},
    {"id": "17", "title": "Building a REST API"},
    {"id": "18", "title": "Authentication Basics"},
    {"id": "19", "title": "Packaging & Deployment"},
    {"id": "20", "title": "Final Project: Mini Web App"},
]

LESSONS = {
    "01": {
        "title": "Python Basics",
        "topics": [
            "Running Python (REPL and scripts)",
            "Variables and basic types (int, float, str, bool)",
            "Simple input and output",
            "Comments and basic style",
        ],
        "examples": [
            "x = 10\npi = 3.14\nname = 'Renzo'\nprint(x, pi, name)",
            "name = input('Enter your name: ')\nprint('Hello,', name)",
        ],
    },
    "02": {
        "title": "Control Flow",
        "topics": [
            "Boolean expressions",
            "if / elif / else",
            "for loops",
            "while loops",
            "break and continue",
        ],
        "examples": [
            "x = 7\nif x > 5:\n    print('big')\nelse:\n    print('small')",
            "for i in range(5):\n    print(i)",
            "n = 3\nwhile n > 0:\n    print(n)\n    n -= 1",
        ],
    },
    "03": {
        "title": "Functions",
        "topics": [
            "Defining functions with def",
            "Parameters and return values",
            "Docstrings",
            "Default arguments",
        ],
        "examples": [
            "def square(x):\n    return x * x\n\nprint(square(4))",
            "def greet(name='world'):\n    print(f'Hello, {name}!')",
        ],
    },
    "04": {
        "title": "Data Structures",
        "topics": [
            "Lists",
            "Tuples",
            "Dictionaries",
            "Sets",
            "Basic list/dict operations",
        ],
        "examples": [
            "nums = [1, 2, 3]\nnums.append(4)\nprint(nums)",
            "user = {'name': 'Renzo', 'role': 'builder'}\nprint(user['name'])",
            "unique = set([1, 2, 2, 3])\nprint(unique)",
        ],
    },
    "05": {
        "title": "Modules & Packages",
        "topics": [
            "Importing modules",
            "The Python standard library",
            "Creating your own modules",
            "__name__ == '__main__'",
        ],
        "examples": [
            "import math\nprint(math.sqrt(16))",
            "# my_module.py\ndef add(a, b):\n    return a + b",
        ],
    },
    "06": {
        "title": "File I/O",
        "topics": [
            "Opening files",
            "Reading and writing text",
            "The with statement",
        ],
        "examples": [
            "with open('notes.txt', 'w') as f:\n    f.write('Hello file!')",
            "with open('notes.txt') as f:\n    print(f.read())",
        ],
    },
    "07": {
        "title": "Error Handling",
        "topics": [
            "Exceptions",
            "try / except / finally",
            "Raising exceptions",
        ],
        "examples": [
            "try:\n    x = int('not a number')\nexcept ValueError:\n    print('Invalid integer')",
            "raise ValueError('Bad value')",
        ],
    },
    "08": {
        "title": "Virtual Environments & pip",
        "topics": [
            "Why virtual environments matter",
            "Creating and activating a venv",
            "Installing packages with pip",
            "Freezing requirements",
        ],
        "examples": [
            "# python -m venv venv\n# source venv/bin/activate\n# pip install requests",
            "# pip freeze > requirements.txt",
        ],
    },
    "09": {
        "title": "Working With APIs (requests)",
        "topics": [
            "HTTP basics",
            "GET requests",
            "Status codes",
            "Parsing JSON responses",
        ],
        "examples": [
            "import requests\nresp = requests.get('https://api.github.com')\nprint(resp.status_code)",
            "data = resp.json()\nprint(data.keys())",
        ],
    },
    "10": {
        "title": "JSON & Data Parsing",
        "topics": [
            "JSON format",
            "json.dumps and json.loads",
            "Reading JSON from a file",
        ],
        "examples": [
            "import json\npayload = {'x': 1, 'y': 2}\ntext = json.dumps(payload)\nprint(text)",
            "data = json.loads(text)\nprint(data['x'])",
        ],
    },
    "11": {
        "title": "Intro to Flask",
        "topics": [
            "What Flask is",
            "Creating a basic app",
            "Running the dev server",
        ],
        "examples": [
            "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return 'Hello, CyberArena!'",
        ],
    },
    "12": {
        "title": "Flask Routing & Views",
        "topics": [
            "Route decorators",
            "Dynamic segments",
            "URL parameters",
        ],
        "examples": [
            "@app.route('/user/<name>')\ndef user(name):\n    return f'Hello {name}'",
        ],
    },
    "13": {
        "title": "Templates & Jinja2",
        "topics": [
            "Rendering templates",
            "Template variables",
            "Loops and conditionals in Jinja2",
        ],
        "examples": [
            "from flask import render_template\n@app.route('/dashboard')\ndef dashboard():\n    stats = {'visits': 10}\n    return render_template('dashboard.html', stats=stats)",
        ],
    },
    "14": {
        "title": "Forms & POST Requests",
        "topics": [
            "HTML forms",
            "GET vs POST",
            "Accessing form data in Flask",
        ],
        "examples": [
            "@app.route('/submit', methods=['GET', 'POST'])\ndef submit():\n    if request.method == 'POST':\n        name = request.form['name']\n        return f'Received {name}'\n    return render_template('form.html')",
        ],
    },
    "15": {
        "title": "Databases With SQLite",
        "topics": [
            "What SQLite is",
            "Connecting to a database",
            "Creating tables and inserting rows",
        ],
        "examples": [
            "import sqlite3\nconn = sqlite3.connect('data.db')\ncur = conn.cursor()\ncur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')\nconn.commit()",
        ],
    },
    "16": {
        "title": "ORM Basics (SQLAlchemy style)",
        "topics": [
            "What an ORM is",
            "Defining models",
            "Creating and querying objects",
        ],
        "examples": [
            "# Pseudo‑code style\nfrom sqlalchemy import Column, Integer, String\nfrom sqlalchemy.orm import declarative_base\nBase = declarative_base()\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    name = Column(String)",
        ],
    },
    "17": {
        "title": "Building a REST API",
        "topics": [
            "JSON responses in Flask",
            "HTTP verbs (GET, POST, PUT, DELETE)",
            "Returning proper status codes",
        ],
        "examples": [
            "from flask import jsonify\n@app.route('/api/status')\ndef api_status():\n    return jsonify({'status': 'ok'})",
        ],
    },
    "18": {
        "title": "Authentication Basics",
        "topics": [
            "Why auth matters",
            "Hashing passwords",
            "Cookies / sessions basics",
        ],
        "examples": [
            "import hashlib\npassword = 'secret'\nhash_value = hashlib.sha256(password.encode()).hexdigest()\nprint(hash_value)",
        ],
    },
    "19": {
        "title": "Packaging & Deployment",
        "topics": [
            "Project structure",
            "requirements.txt",
            "Environment variables",
            "Basic deployment concepts",
        ],
        "examples": [
            "# pip freeze > requirements.txt\n# export FLASK_ENV=production",
        ],
    },
    "20": {
        "title": "Final Project: Mini Web App",
        "topics": [
            "Choosing a simple idea",
            "Designing routes and templates",
            "Persisting data",
            "Documenting the project",
        ],
        "examples": [
            "# Example: Task tracker app\n# Routes: list tasks, add task, delete task\n# Templates: index.html, layout.html",
        ],
    },
}

LABS = {
    "lab01": {
        "title": "Variables & Types",
        "instructions": "Create variables for your name, age, and favorite language. Print them in one formatted sentence.",
        "hint": "Use f-strings: f'My name is {name} and I am {age} years old.'",
    },
    "lab02": {
        "title": "Control Flow",
        "instructions": "Write a program that prints 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, and 'FizzBuzz' for multiples of both from 1 to 50.",
        "hint": "Use if/elif/else and the modulo operator (%).",
    },
    "lab03": {
        "title": "Functions",
        "instructions": "Write a function that takes a list of numbers and returns the average.",
        "hint": "Use sum(list) and len(list).",
    },
    "lab04": {
        "title": "Lists & Dictionaries",
        "instructions": "Given a sentence, build a dictionary that maps each word to its count.",
        "hint": "Split on spaces and update a dict inside a loop.",
    },
    "lab05": {
        "title": "Modules",
        "instructions": "Create a module with math helper functions (add, subtract, multiply). Import and use it in another script.",
        "hint": "Put functions in one .py file, then import that file in another.",
    },
    "lab06": {
        "title": "File Reader",
        "instructions": "Write a script that reads a text file and prints the number of lines, words, and characters.",
        "hint": "Use len(lines), len(words), and len(content).",
    },
    "lab07": {
        "title": "Error Handling",
        "instructions": "Write a script that asks for a number and handles non-numeric input gracefully.",
        "hint": "Wrap int(input(...)) in try/except ValueError.",
    },
    "lab08": {
        "title": "Virtual Environment Drill",
        "instructions": "Create a virtual environment, activate it, install 'requests', and freeze dependencies.",
        "hint": "Use python -m venv venv, source venv/bin/activate, pip install, pip freeze.",
    },
    "lab09": {
        "title": "API Call",
        "instructions": "Call a public API (e.g., api.github.com) and print the response status and one interesting field from the JSON.",
        "hint": "Use requests.get(url).json() and inspect the keys.",
    },
    "lab10": {
        "title": "JSON File",
        "instructions": "Write a Python dict to a JSON file, then read it back and print a field.",
        "hint": "Use json.dump and json.load with open(..., 'w') / open(...).",
    },
    "lab11": {
        "title": "First Flask App",
        "instructions": "Create a minimal Flask app with a single route that returns 'Hello from Python Lab'.",
        "hint": "Use Flask(__name__), @app.route('/') and app.run().",
    },
    "lab12": {
        "title": "Dynamic Route",
        "instructions": "Add a route /hello/<name> that returns a personalized greeting.",
        "hint": "Use a route parameter and an f-string.",
    },
    "lab13": {
        "title": "Template Rendering",
        "instructions": "Create a template that displays a list of tasks passed from the Flask view.",
        "hint": "Use render_template and a for-loop in Jinja2.",
    },
    "lab14": {
        "title": "Handling Forms",
        "instructions": "Build a form that lets the user submit their name and then thanks them on POST.",
        "hint": "Check request.method and access request.form['name'].",
    },
    "lab15": {
        "title": "SQLite Table",
        "instructions": "Create a database file and a 'notes' table, then insert one note.",
        "hint": "Use sqlite3.connect and execute an INSERT.",
    },
    "lab16": {
        "title": "Simple ORM Model",
        "instructions": "Define a User model with id and name, then create and query one user (pseudo-code is fine).",
        "hint": "Think in terms of a class mapped to a table.",
    },
    "lab17": {
        "title": "JSON API Endpoint",
        "instructions": "Create a Flask route /api/ping that returns JSON {'status': 'ok'}.",
        "hint": "Use jsonify in the view.",
    },
    "lab18": {
        "title": "Password Hashing",
        "instructions": "Write a function that hashes a plaintext password and verifies it by comparison.",
        "hint": "Use hashlib.sha256(password.encode()).hexdigest().",
    },
    "lab19": {
        "title": "Prepare for Deployment",
        "instructions": "Create a requirements.txt for your Flask app and a short README explaining how to run it.",
        "hint": "Use pip freeze and write clear run instructions.",
    },
    "lab20": {
        "title": "Final Project",
        "instructions": "Design and implement a small Flask app (e.g., todo list, notes, bookmarks) using routes, templates, and persistent storage.",
        "hint": "Reuse patterns from earlier labs: forms, templates, and a simple DB or JSON file.",
    },
}
