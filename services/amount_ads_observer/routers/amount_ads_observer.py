from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query
from starlette.responses import Response

from services.amount_ads_observer.container import AmountAdsObserverContainer
from services.amount_ads_observer.dal import AdsObserversRepository
from services.amount_ads_observer.schemas.ads_observer import AdsObserverCreate, AdsObserver
from services.worker.app import save_curr_ads_amount


router = APIRouter(prefix='/ads/amount/observer')


@router.get('/stat')
async def get_stat(location_id: int = Query(), query: str = Query()):
    save_curr_ads_amount.delay(
        location_id=location_id,
        query=query
    )
    return Response(status_code=HTTPStatus.NO_CONTENT)


@router.post('/add', response_model=AdsObserver)
@inject
async def add_observation(
    ads_observer_data: AdsObserverCreate,
    ads_observers_repo: AdsObserversRepository = Depends(
        Provide[AmountAdsObserverContainer.ads_observers_repository]
    )
):
    ads_observer = await ads_observers_repo.add_one(ads_observer_data)
    save_curr_ads_amount.delay(
        ads_observer_id=ads_observer.id,
        location_id=ads_observer.location_id,
        query=ads_observer.query
    )
    return ads_observer
