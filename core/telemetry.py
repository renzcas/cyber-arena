# core/telemetry.py

import threading
import json
from typing import Any, Dict, Set


class Telemetry:
    """
    Manages WebSocket clients and broadcasts live Arena state.
    """

    def __init__(self):
        self.clients: Set[Any] = set()
        self._lock = threading.Lock()

    def register(self, ws):
        with self._lock:
            self.clients.add(ws)

    def unregister(self, ws):
        with self._lock:
            if ws in self.clients:
                self.clients.remove(ws)

    def broadcast(self, state: Dict[str, Any]):
        """
        Send the latest Arena state to all connected clients.
        """
        message = json.dumps(state)

        dead = []
        with self._lock:
            for ws in self.clients:
                try:
                    ws.send(message)
                except Exception:
                    dead.append(ws)

        # Clean up dead sockets
        for ws in dead:
            self.unregister(ws)
