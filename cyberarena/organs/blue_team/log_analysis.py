def simulate_log_analysis(sample: str):
    if not sample:
        return ["No log sample provided"]

    return [
        f"Analyzing log sample: {sample}",
        "Pattern match: benign (simulated)",
        "No known IOC signatures detected",
        "Log analysis complete."
    ]
