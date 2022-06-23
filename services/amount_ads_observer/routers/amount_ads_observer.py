from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from services.amount_ads_observer.container import AmountAdsObserverContainer
from services.amount_ads_observer.dal import AdsObserversRepository
from services.amount_ads_observer.schemas.ads_observer import AdsObserverCreate, AdsObserver

router = APIRouter(prefix='/ads/amount/observer')


@router.get('/stat')
async def get_stat():
    pass


@router.post('/add', response_model=AdsObserver)
@inject
async def add_observation(
    ads_observer_data: AdsObserverCreate,
    ads_observers_repo: AdsObserversRepository = Depends(
        Provide[AmountAdsObserverContainer.ads_observers_repository]
    )
):
    return await ads_observers_repo.add_one(ads_observer_data)
