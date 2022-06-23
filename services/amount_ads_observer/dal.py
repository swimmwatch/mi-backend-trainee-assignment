"""
Announcement observer Data Access Layer.
"""
from services.amount_ads_observer.models import AdsObserver
from services.amount_ads_observer.schemas.ads_observer import AdsObserverCreate
from utils.sqlalchemy.dal import SQLAlchemyRepository


class AdsObserversRepository(SQLAlchemyRepository):
    """
    Advert observers repository that uses SQLAlchemy.
    """
    async def add_one(self, ads_observer_data: AdsObserverCreate) -> AdsObserver:
        async with self.session_factory() as session:
            async with session.begin():
                ad_observer = AdsObserver(**ads_observer_data.dict())
                session.add(ad_observer)
                await session.commit()
                return ad_observer
