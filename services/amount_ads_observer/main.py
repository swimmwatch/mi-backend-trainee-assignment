"""
Announcement observer service entrypoint.
"""
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI, Depends

from services.amount_ads_observer.container import \
    AmountAdsObserverContainer
from services.amount_ads_observer.dal import CityRepository
from services.amount_ads_observer.schemas.city import City
from services.amount_ads_observer.utils import async_init_db
from services.worker.app import count

app = FastAPI()
container = AmountAdsObserverContainer()


@app.on_event('startup')
async def wire_container():
    container.wire(modules=[__name__])


@app.on_event('startup')
async def init_db():
    await async_init_db(container.db())


@app.get('/cities', response_model=List[City])
@inject
async def get_cities(
    cities_rep: CityRepository = Depends(
        Provide[AmountAdsObserverContainer.cities_repository]
    )
) -> List[City]:
    cities_records = await cities_rep.get_all()
    count.delay()
    return [
        City(
            id=city_record.id,
            name=city_record.name
        )
        for city_record in cities_records
    ]