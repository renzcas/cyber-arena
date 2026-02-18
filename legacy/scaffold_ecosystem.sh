#!/usr/bin/env bash

echo "🔧 Building CyberArena Ecosystem Scaffold..."
BASE="cyberarena"

# --- Helper: create directory if missing ---
ensure_dir() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
        echo "📁 Created directory: $1"
    fi
}

# --- Helper: create file if missing ---
ensure_file() {
    if [ ! -f "$1" ]; then
        echo -e "$2" > "$1"
        echo "📄 Created file: $1"
    fi
}

# ============================================================
# 1. TELEMETRY
# ============================================================
ensure_dir "$BASE/telemetry"

ensure_file "$BASE/telemetry/events.py" \
"from datetime import datetime
from pydantic import BaseModel

class Event(BaseModel):
    timestamp: float
    type: str
    payload: dict

    @staticmethod
    def make(event_type: str, payload: dict):
        return Event(
            timestamp=datetime.utcnow().timestamp(),
            type=event_type,
            payload=payload
        )
"

ensure_file "$BASE/telemetry/stream.py" \
"from fastapi import WebSocket
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
"

# ============================================================
# 2. ENVIRONMENT
# ============================================================
ensure_dir "$BASE/environment"

ensure_file "$BASE/environment/base_env.py" \
"class BaseEnvironment:
    def reset(self):
        raise NotImplementedError

    def step(self, action):
        raise NotImplementedError
"

ensure_file "$BASE/environment/cyber_env.py" \
"from .base_env import BaseEnvironment

class CyberEnvironment(BaseEnvironment):
    def __init__(self):
        self.state = {}

    def reset(self):
        self.state = {}
        return self.state

    def step(self, action):
        return {'result': 'ok', 'action': action}
"

ensure_file "$BASE/environment/state_adapter.py" \
"class StateAdapter:
    @staticmethod
    def to_event(state):
        return {'state': state}
"

# ============================================================
# 3. ORGAN FACTORY
# ============================================================
ensure_dir "$BASE/organ_factory"

ensure_file "$BASE/organ_factory/registry.py" \
"ORGANS = {}

def register(name, cls):
    ORGANS[name] = cls

def get(name):
    return ORGANS.get(name)
"

ensure_file "$BASE/organ_factory/factory.py" \
"from .registry import get

class OrganFactory:
    @staticmethod
    def create(name, **kwargs):
        cls = get(name)
        if not cls:
            raise ValueError(f'Unknown organ: {name}')
        return cls(**kwargs)
"

ensure_file "$BASE/organ_factory/loader.py" \
"import importlib

def load_module(path):
    return importlib.import_module(path)
"

# ============================================================
# 4. DIRECTOR
# ============================================================
ensure_dir "$BASE/director"

ensure_file "$BASE/director/director.py" \
"class Director:
    def __init__(self, environment):
        self.environment = environment

    def run_step(self, action):
        return self.environment.step(action)
"

ensure_file "$BASE/director/scheduler.py" \
"class Scheduler:
    def schedule(self, tasks):
        return tasks
"

ensure_file "$BASE/director/narrative_hooks.py" \
"class NarrativeHooks:
    @staticmethod
    def before_step(state):
        return state

    @staticmethod
    def after_step(result):
        return result
"

# ============================================================
# 5. FUSION
# ============================================================
ensure_dir "$BASE/fusion"

ensure_file "$BASE/fusion/fusion_engine.py" \
"class FusionEngine:
    def fuse(self, *signals):
        return {'fusion': signals}
"

ensure_file "$BASE/fusion/organ_bridge.py" \
"class OrganBridge:
    def connect(self, organ, environment):
        return True
"

# ============================================================
# 6. NARRATIVE
# ============================================================
ensure_dir "$BASE/narrative"

ensure_file "$BASE/narrative/storyline.py" \
"class Storyline:
    def next_event(self):
        return {'event': 'tick'}
"

ensure_file "$BASE/narrative/events.py" \
"class NarrativeEvent:
    def __init__(self, name):
        self.name = name
"

ensure_file "$BASE/narrative/triggers.py" \
"class Trigger:
    def check(self, state):
        return False
"

echo "✨ CyberArena ecosystem scaffold complete!"
