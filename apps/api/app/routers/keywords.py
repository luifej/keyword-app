from fastapi import APIRouter
from worker.tasks import discover_ideas

router = APIRouter()

@router.post("/discover")
def discover(payload: dict):
    # expected payload: { "seed": str, "country": "US", "lang": "en" }
    task = discover_ideas.delay(payload)
    return {"task_id": task.id}
