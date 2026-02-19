from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import os

from cyberarena.telemetry.stream import stream
from cyberarena.telemetry.events import Event

# --- NEW IMPORTS ---
from cyberarena.fusion.fusion_openclaw import ENERGY_ENGINE
from core.scoring_engine import ScoringEngine
from pydantic import BaseModel
from typing import List, Tuple

app = FastAPI()

# Serve cockpit static files
app.mount(
    "/cockpit",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "cockpit")),
    name="cockpit"
)

SCORING_ENGINE = ScoringEngine()

# -----------------------------
# ENERGY TELEMETRY ENDPOINT
# -----------------------------
class EnergySeries(BaseModel):
    agent_id: str
    role: str
    points: List[Tuple[float, float, float]]

class EnergyResponse(BaseModel):
    series: List[EnergySeries]

@app.get("/telemetry/energy", response_model=EnergyResponse)
def get_energy():
    roles = {
        "agent_red_1": "RED",
        "agent_blue_1": "BLUE",
        "agent_purple_1": "PURPLE",
    }
    all_series = ENERGY_ENGINE.get_all_series()
    return EnergyResponse(
        series=[
            EnergySeries(agent_id=aid, role=roles.get(aid, "UNKNOWN"), points=pts)
            for aid, pts in all_series.items()
        ]
    )

# -----------------------------
# PHASE SPACE ENDPOINT
# -----------------------------
class PhasePoint(BaseModel):
    t: float
    x: float
    y: float

class PhaseSeries(BaseModel):
    agent_id: str
    role: str
    coord: str
    points: List[PhasePoint]

class PhaseResponse(BaseModel):
    series: List[PhaseSeries]

@app.get("/telemetry/phase_space", response_model=PhaseResponse)
def get_phase_space():
    roles = {
        "agent_red_1": "RED",
        "agent_blue_1": "BLUE",
        "agent_purple_1": "PURPLE",
    }
    coord_map = {
        "agent_red_1": "anomaly_pressure",
        "agent_blue_1": "system_risk",
        "agent_purple_1": "symbolic_load",
    }

    history = ENERGY_ENGINE.get_state_history()
    series = []

    for agent_id, states in history.items():
        role = roles.get(agent_id, "UNKNOWN")
        coord = coord_map.get(agent_id)
        if not coord:
            continue

        pts = [
            PhasePoint(t=st.t, x=st.q.get(coord, 0.0), y=st.dq.get(coord, 0.0))
            for st in states
        ]

        series.append(
            PhaseSeries(agent_id=agent_id, role=role, coord=coord, points=pts)
        )

    return PhaseResponse(series=series)

# -----------------------------
# SCORING ENDPOINT
# -----------------------------
class ScoreResponse(BaseModel):
    red: int
    blue: int
    purple: int

@app.get("/telemetry/scoring", response_model=ScoreResponse)
def get_scores():
    s = SCORING_ENGINE.snapshot()
    return ScoreResponse(red=s["RED"], blue=s["BLUE"], purple=s["PURPLE"])
