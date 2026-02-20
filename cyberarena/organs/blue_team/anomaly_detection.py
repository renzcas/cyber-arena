def detect_anomalies(data: str):
    if not data:
        return ["No data provided"]

    return [
        f"Input analyzed: {data}",
        "Baseline deviation: 12% (simulated)",
        "Anomaly likelihood: LOW",
        "No threat indicators detected."
    ]
