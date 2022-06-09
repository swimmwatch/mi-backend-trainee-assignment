from celery import Celery
from dependency_injector.wiring import inject, Provide
from redis import Redis

from services.worker.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from services.worker.container import WorkerContainer

celery = Celery(
    'tasks',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)


@celery.on_after_configure.connect
def init_di_container(sender, **kwargs):
    worker_container = WorkerContainer()
    worker_container.wire(modules=[__name__])


@celery.task
@inject
def count(redis_client: Redis = Provide[WorkerContainer.redis_client]):
    redis_client.incr('counter', 1)
