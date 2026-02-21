from datetime import datetime
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

