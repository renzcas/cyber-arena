from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import os

from cyberarena.telemetry.stream import stream
from cyberarena.telemetry.events import Event

app = FastAPI()

# Serve cockpit static files
app.mount(
    "/cockpit",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "cockpit")),
    name="cockpit"
)

@app.get("/")
def home():
    return {"status": "CyberArena Ecosystem Running"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await stream.connect(ws)
    try:
        while True:
            msg = await ws.receive_text()
            event = Event.make("client_message", {"msg": msg})
            await stream.broadcast(event)
    except:
        await stream.disconnect(ws)
