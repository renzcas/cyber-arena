from fastapi import APIRouter
from .models import Target
from .registry import register_target, list_targets

router = APIRouter(prefix="/targets")

@router.post("/register")
def register(target: Target):
    register_target(target)
    return {"status": "registered", "target": target}

@router.get("/")
def get_targets():
    return list_targets()
