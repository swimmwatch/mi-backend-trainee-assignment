from celery import Celery
from dependency_injector.wiring import inject, Provide
from loguru import logger

from services.private_avito_api_executor import GetAmountAdsRequest
from services.private_avito_api_executor.grpc_client import PrivateAvitoApiExecutorGrpcClient
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
def save_curr_ads_amount(
    location_id: int,
    query: str,
    private_avito_api_executor_client: PrivateAvitoApiExecutorGrpcClient =
    Provide[WorkerContainer.private_avito_api_executor_client]
):
    req = GetAmountAdsRequest(
        location_id=location_id,
        query=query
    )
    res = private_avito_api_executor_client.stub.get_amount_ads(req)
    logger.info(res.amount)
