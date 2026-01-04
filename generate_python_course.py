import os

# -----------------------------
# Folder + file definitions
# -----------------------------

COURSE_STRUCTURE = {
    "module_1_foundations": {
        "lessons": [
            "1_basics.md",
            "2_control_flow.md",
            "3_collections.md",
            "4_functions.md",
            "5_files.md",
        ],
        "exercises": [
            "ex1_greeting.py",
            "ex2_even_odd.py",
            "ex3_even_filter.py",
            "ex4_average.py",
            "ex5_json_edit.py",
        ],
    },

    "module_2_intermediate": {
        "lessons": [
            "1_oop.md",
            "2_modules.md",
            "3_errors.md",
            "4_venv.md",
        ],
        "exercises": [
            "ex1_bank_account.py",
            "ex2_module_import.py",
            "ex3_safe_divide.py",
            "ex4_create_venv.txt",
        ],
    },

    "module_3_apis": {
        "lessons": [
            "1_http.md",
            "2_fastapi.md",
            "3_async_streaming.md",
        ],
        "exercises": [
            "ex1_call_api.py",
            "ex2_fastapi_hello.py",
            "ex3_stream_timestamps.py",
        ],
    },

    "module_4_automation": {
        "lessons": [
            "1_os.md",
            "2_scraping.md",
            "3_cli.md",
        ],
        "exercises": [
            "ex1_file_sorter.py",
            "ex2_scrape_headlines.py",
            "ex3_cli_renamer.py",
        ],
    },

    "module_5_data": {
        "lessons": [
            "1_numpy.md",
            "2_pandas.md",
            "3_visualization.md",
        ],
        "exercises": [
            "ex1_dot_product.py",
            "ex2_csv_stats.py",
            "ex3_histogram.py",
        ],
    },

    "module_6_ml": {
        "lessons": [
            "1_pytorch.md",
            "2_transformers.md",
        ],
        "exercises": [
            "ex1_linear_regression.py",
            "ex2_bert_embeddings.py",
        ],
    },

    "module_7_agents": {
        "lessons": [
            "1_event_loops.md",
            "2_state_machines.md",
            "3_dashboards.md",
            "4_entropy_models.md",
        ],
        "exercises": [
            "ex1_pulse_generator.py",
            "ex2_role_bifurcation.py",
            "ex3_live_dashboard.py",
            "ex4_collapse_detector.py",
        ],
    },

    "module_8_deployment": {
        "lessons": [
            "1_git.md",
            "2_docker.md",
            "3_cloud.md",
        ],
        "exercises": [
            "ex1_new_repo.txt",
            "ex2_dockerize_fastapi.py",
            "ex3_deploy_cloud.txt",
        ],
    },
}

CAPSTONE_STRUCTURE = {
    "capstone/agentdash_clone/backend/engines": [
        "pulse_engine.py",
        "entropy_engine.py",
        "collapse_detector.py",
        "role_bifurcation.py",
    ],
    "capstone/agentdash_clone/backend": [
        "main.py",
    ],
    "capstone/agentdash_clone/dashboard/components": [
        "live_charts.py",
        "state_panels.py",
    ],
    "capstone/agentdash_clone/dashboard": [
        "app.py",
    ],
    "capstone/agentdash_clone": [
        "README.md",
    ],
}

# -----------------------------
# Create folders + files
# -----------------------------

def create_structure(base="python_course"):
    print(f"Creating course structure in: {base}")

    for module, content in COURSE_STRUCTURE.items():
        module_path = os.path.join(base, module)

        # Lessons
        lessons_path = os.path.join(module_path, "lessons")
        os.makedirs(lessons_path, exist_ok=True)
        for lesson in content["lessons"]:
            open(os.path.join(lessons_path, lesson), "a").close()

        # Exercises
        exercises_path = os.path.join(module_path, "exercises")
        os.makedirs(exercises_path, exist_ok=True)
        for exercise in content["exercises"]:
            open(os.path.join(exercises_path, exercise), "a").close()

    # Capstone
    for folder, files in CAPSTONE_STRUCTURE.items():
        folder_path = os.path.join(base, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            open(os.path.join(folder_path, file), "a").close()

    print("Course structure created successfully!")


if __name__ == "__main__":
    create_structure()
