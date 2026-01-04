import os
from pathlib import Path

# Root directory for CyberArena
ROOT = Path("CyberArena")

# Organ names
ORGANS = [
    "memory",
    "replay",
    "telemetry",
    "scoring",
    "curriculum",
    "network_graph"
]

def make_dir(path: Path):
    """Create a directory if it doesn't exist."""
    if not path.exists():
        path.mkdir(parents=True)
        print(f"[+] Created directory: {path}")
    else:
        print(f"[=] Directory already exists: {path}")

def make_file(path: Path, content=""):
    """Create a file if it doesn't exist."""
    if not path.exists():
        path.write_text(content)
        print(f"[+] Created file: {path}")
    else:
        print(f"[=] File already exists: {path}")

def main():
    print("\n🚀 Building CyberArena folder structure...\n")

    # Create root
    make_dir(ROOT)

    # Create organs directory
    organs_dir = ROOT / "organs"
    make_dir(organs_dir)

    # Create each organ folder
    for organ in ORGANS:
        make_dir(organs_dir / organ)

    # Create data directory + empty DB file
    data_dir = ROOT / "data"
    make_dir(data_dir)
    make_file(data_dir / "cyberarena.db", "")  # empty placeholder

    # Create interfaces directory
    interfaces_dir = ROOT / "interfaces"
    make_dir(interfaces_dir)

    # Create db.py and models.py placeholders
    make_file(interfaces_dir / "db.py", "# db.py — database interface\n")
    make_file(interfaces_dir / "models.py", "# models.py — ORM models\n")

    print("\n🎉 CyberArena structure created successfully!\n")

if __name__ == "__main__":
    main()
