# python_lab/curriculum.py

COURSE_OUTLINE = [
    {"id": "01", "title": "Python Basics"},
    {"id": "02", "title": "Control Flow"},
    {"id": "03", "title": "Functions"},
    {"id": "04", "title": "Object-Oriented Python"},
    {"id": "05", "title": "Modules & Packages"},
    {"id": "06", "title": "Flask Web Apps"},
]

LESSONS = {
    "01": {
        "title": "Python Basics",
        "content": [
            "Variables & Types",
            "Input/Output",
            "Basic Operators",
            "Strings & Formatting"
        ],
        "examples": [
            "x = 10",
            "name = input('Enter your name: ')",
        ]
    },
    "02": {
        "title": "Control Flow",
        "content": ["if/else", "for loops", "while loops"],
        "examples": ["for i in range(5): print(i)"]
    },
}

LABS = {
    "lab01": {
        "title": "Variables Lab",
        "instructions": "Create variables for name, age, and city. Print them in a formatted sentence."
    },
    "lab02": {
        "title": "Loops Lab",
        "instructions": "Write a loop that prints numbers 1–50 but skips multiples of 3."
    },
}
