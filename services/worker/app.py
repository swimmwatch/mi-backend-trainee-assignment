from datetime import datetime, timedelta

from celery import Celery
from dependency_injector.wiring import inject, Provide

from services.amount_ads_observer.models import AdsObserver, AdsObserverStat
from services.db import Database
from services.private_avito_api_executor import GetAmountAdsRequest
from services.private_avito_api_executor.grpc_client import PrivateAvitoApiExecutorGrpcClient
from services.worker.config import worker_settings
from services.worker.container import WorkerContainer
from utils.datetime import get_uts_from_datatime

celery = Celery(
    'tasks',
    broker=worker_settings.celery_broker_url,
    backend=worker_settings.celery_result_backend
)


@celery.on_after_configure.connect
def init_di_container(sender, **kwargs):
    worker_container = WorkerContainer()
    worker_container.wire(modules=[__name__])


@celery.task
@inject
def save_curr_ads_amount(
        ads_observer_id: int,
        location_id: int,
        query: str,
        db: Database = Provide[WorkerContainer.db],
        private_avito_api_executor_client: PrivateAvitoApiExecutorGrpcClient =
        Provide[WorkerContainer.private_avito_api_executor_client]
):
    with db.session() as session:
        exists = session.query(AdsObserver) \
                    .filter_by(id=ads_observer_id) \
                    .first()
        if not exists:
            return

    req = GetAmountAdsRequest(
        location_id=location_id,
        query=query
    )
    res = private_avito_api_executor_client.stub.get_amount_ads(req)

    now = datetime.utcnow()
    uts_now = get_uts_from_datatime(now)
    with db.session() as session:
        ads_observer_stat = AdsObserverStat(
            ads_observer_id=ads_observer_id,
            timestamp=uts_now,
            amount=res.amount
        )
        session.add(ads_observer_stat)
        session.commit()

    in_hour = now + timedelta(minutes=1)
    save_curr_ads_amount.apply_async(
        (
            ads_observer_id,
            location_id,
            query
        ),
        eta=in_hour
    )
