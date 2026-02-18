from fastapi import WebSocket
from .events import Event

class EventStream:
    def __init__(self):
        self.connections = set()

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.connections.add(ws)

    async def disconnect(self, ws: WebSocket):
        self.connections.remove(ws)

    async def broadcast(self, event: Event):
        dead = []
        for ws in self.connections:
            try:
                await ws.send_json(event.dict())
            except:
                dead.append(ws)
        for ws in dead:
            await self.disconnect(ws)

stream = EventStream()

