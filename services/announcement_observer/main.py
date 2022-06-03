"""
Announcement observer service entrypoint.
"""
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI, Depends

from services.announcement_observer.container import AnnouncementObserverContainer
from services.announcement_observer.dal import CityRepository
from services.announcement_observer.schemas.city import City
from services.announcement_observer.utils import async_init_db

app = FastAPI()
container = AnnouncementObserverContainer()


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
        Provide[AnnouncementObserverContainer.cities_repository]
    )
) -> List[City]:
    cities_records = await cities_rep.get_all()
    return [
        City(
            id=city_record.id,
            name=city_record.name
        )
        for city_record in cities_records
    ]
