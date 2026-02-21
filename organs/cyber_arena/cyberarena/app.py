# cyberarena/app.py

import asyncio
import os
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles

# Environment + Director
from cyberarena.environment.cyber_env import CyberEnvironment
from cyberarena.director.director import Director

# Telemetry
from cyberarena.telemetry.stream import stream
from cyberarena.telemetry.events import Event


# ---------------------------------------------------------
# FastAPI App
# ---------------------------------------------------------
app = FastAPI(title="CyberArena Ecosystem")


# ---------------------------------------------------------
# Cockpit Static Files
# ---------------------------------------------------------
COCKPIT_DIR = os.path.join(os.path.dirname(__file__), "cockpit")

app.mount(
    "/cockpit",
    StaticFiles(directory=COCKPIT_DIR),
    name="cockpit"
)


# ---------------------------------------------------------
# Initialize Environment + Director
# ---------------------------------------------------------
# Later you can pass an InfoPhyzx engine:
# env = CyberEnvironment(infophyzx_engine=my_engine)
env = CyberEnvironment()
director = Director()


# ---------------------------------------------------------
# Startup: Begin Environment Loop
# ---------------------------------------------------------
@app.on_event("startup")
async def startup_event():
    """
    When the server starts, begin the environment heartbeat loop.
    """
    asyncio.create_task(environment_loop())


async def environment_loop():
    """
    Runs forever. Calls env.tick() every second.
    Then passes the environment state to the Director.
    """
    while True:
        await env.tick()
        await director.on_tick(env.state)


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------
@app.get("/")
def home():
    return {"status": "CyberArena Ecosystem Running"}


# ---------------------------------------------------------
# WebSocket Endpoint
# ---------------------------------------------------------
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    """
    Handles WebSocket connections from cockpit panels.
    """
    await stream.connect(ws)

    try:
        while True:
            msg = await ws.receive_text()
            event = Event.make("client_message", {"msg": msg})
            await stream.broadcast(event)

    except Exception:
        await stream.disconnect(ws)
