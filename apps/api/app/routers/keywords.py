from fastapi import APIRouter
import os
from worker.tasks import discover_ideas

router = APIRouter()

@router.post("/discover")
def discover(payload: dict):
    if os.getenv("SYNC_MODE") == "1":
        return discover_ideas(payload)   # correr sin Celery/Redis
    task = discover_ideas.delay(payload) # Celery (cuando lo actives)
    return {"task_id": task.id}
