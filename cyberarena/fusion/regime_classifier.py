from typing import List
from statistics import variance


def classify_regime(x_vals: List[float], v_vals: List[float], thresholds: dict) -> str:
    if len(x_vals) < 3 or len(v_vals) < 3:
        return "INTERMEDIATE"

    x = x_vals[-1]
    v = abs(v_vals[-1])
    a = abs(v_vals[-1] - v_vals[-2])
    var_x = variance(x_vals[-min(len(x_vals), 20):])

    if x > thresholds["x_critical"] and v > thresholds["v_critical"]:
        return "CRITICAL"
    if v > thresholds["v_chaotic"] and a > thresholds["a_chaotic"] and var_x > thresholds["var_chaotic"]:
        return "CHAOTIC"
    if v < thresholds["v_stable"] and a < thresholds["a_stable"] and var_x < thresholds["var_stable"]:
        return "STABLE"
    return "INTERMEDIATE"
