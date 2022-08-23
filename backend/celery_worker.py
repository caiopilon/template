import os

from dotenv import load_dotenv

from celery import Celery, shared_task


load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

celery.autodiscover_tasks()

celery.conf.beat_schedule = {
    "test_task": {
        "task": "api.tasks.test",
        "schedule": 1,
    }
}