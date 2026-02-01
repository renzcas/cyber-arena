def get_arena_state():
    return {
        "red_team": {"status": "active"},
        "blue_team": {"status": "defending"},
        "grey_team": {"status": "idle"},
        "metrics": {
            "attack_intensity": 0.42,
            "defense_load": 0.31
        },
        "scenario": {
            "name": "Basic Recon",
            "phase": "initial"
        }
    }
