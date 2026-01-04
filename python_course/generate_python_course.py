import os
from pathlib import Path
import shutil

# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------

BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / "templates"
OUTPUT_DIR = BASE_DIR / "course"

MODULES = [f"module_{i}" for i in range(1, 9)]

# ---------------------------------------------------------
# UTILITIES
# ---------------------------------------------------------

def log(msg):
    print(f"[OK] {msg}")

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------
# METADATA INJECTION
# ---------------------------------------------------------

def inject_metadata(content: str, module_num: int, lesson_num: int, author="Renzo"):
    """
    Extracts title from first line (# Title)
    Injects CyberArena metadata block.
    """
    lines = content.strip().split("\n")
    first_line = lines[0].strip()

    if first_line.startswith("#"):
        title = first_line.lstrip("#").strip()
        body = "\n".join(lines[1:])
    else:
        title = f"Lesson {lesson_num}"
        body = content

    metadata = f"""---
title: {title}
difficulty: beginner
panel: python_course
module: {module_num}
lesson: {lesson_num}
tags: [python, foundations]
type: lesson
version: 1.0
author: {author}
---

"""

    return metadata + body

# ---------------------------------------------------------
# FILE WRITING
# ---------------------------------------------------------

def write_file(path: Path, content: str):
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    log(f"Wrote {path}")

# ---------------------------------------------------------
# INDEX GENERATION
# ---------------------------------------------------------

def generate_index():
    index_path = OUTPUT_DIR / "INDEX.md"
    lines = ["# Python Course Index\n"]

    for module in MODULES:
        lines.append(f"## {module.replace('_', ' ').title()}")
        module_path = OUTPUT_DIR / module / "lessons"

        if not module_path.exists():
            continue

        for file in sorted(module_path.iterdir()):
            if file.suffix == ".md":
                lesson_num = file.stem.split("_")[0]
                title = file.stem.split("_", 1)[1].replace("_", " ").title()
                lines.append(f"- **Lesson {lesson_num}: {title}**")

        lines.append("")

    write_file(index_path, "\n".join(lines))

# ---------------------------------------------------------
# MAIN BUILD PROCESS
# ---------------------------------------------------------

def build_course():
    log("Starting Python Course build...")

    # Create template folders if missing
    for module in MODULES:
        ensure_dir(TEMPLATE_DIR / "lessons" / module)
        ensure_dir(TEMPLATE_DIR / "exercises" / module)

    ensure_dir(TEMPLATE_DIR / "capstone" / "backend")
    ensure_dir(TEMPLATE_DIR / "capstone" / "dashboard")
    ensure_dir(TEMPLATE_DIR / "capstone" / "engines")

    # Process lessons
    for module in MODULES:
        module_num = int(module.split("_")[1])
        lesson_dir = TEMPLATE_DIR / "lessons" / module

        for file in sorted(lesson_dir.iterdir()):
            if file.suffix != ".md":
                continue

            lesson_num = int(file.stem.split("_")[0])
            content = file.read_text(encoding="utf-8")

            final = inject_metadata(content, module_num, lesson_num)

            out_path = OUTPUT_DIR / module / "lessons" / file.name
            write_file(out_path, final)

    # Process exercises (copied as-is)
    for module in MODULES:
        exercise_dir = TEMPLATE_DIR / "exercises" / module

        for file in sorted(exercise_dir.iterdir()):
            if file.suffix != ".py":
                continue

            out_path = OUTPUT_DIR / module / "exercises" / file.name
            shutil.copy(file, out_path)
            log(f"Copied exercise {file} → {out_path}")

    # Process capstone (copied as-is)
    cap_dirs = ["backend", "dashboard", "engines"]
    for sub in cap_dirs:
        src = TEMPLATE_DIR / "capstone" / sub
        dst = OUTPUT_DIR / "capstone" / sub
        ensure_dir(dst)

        for file in src.iterdir():
            shutil.copy(file, dst / file.name)
            log(f"Copied capstone file {file} → {dst / file.name}")

    # Generate index
    generate_index()

    log("Python Course build complete!")

# ---------------------------------------------------------
# RUN
# ---------------------------------------------------------

if __name__ == "__main__":
    build_course()
