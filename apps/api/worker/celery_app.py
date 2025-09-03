import os
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

celery_app = Celery(
    __name__,
    broker=REDIS_URL,
    backend=os.getenv("REDIS_BACKEND_URL", "redis://redis:6379/1"),
    include=["app.worker.tasks"],
)

celery_app.conf.task_routes = {"app.worker.tasks.*": {"queue": "keywords"}}
