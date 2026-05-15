from celery import Celery


celery = Celery(
    "f1_ai_assistant",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=[
        "app.tasks.race_tasks"
    ]
)