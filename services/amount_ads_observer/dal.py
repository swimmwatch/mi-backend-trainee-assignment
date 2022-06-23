"""
Announcement observer Data Access Layer.
"""
from services.amount_ads_observer.models import AdObserver
from utils.sqlalchemy.dal import SQLAlchemyRepository


class AdObserversRepository(SQLAlchemyRepository):
    """
    Advert observers repository that uses SQLAlchemy.
    """
    async def add_one(self, location_id: int, query: str) -> AdObserver:
        async with self.session_factory() as session:
            async with session.begin():
                ad_observer = AdObserver(
                    location_id=location_id,
                    query=query
                )
                session.add(ad_observer)
                await session.commit()
                return ad_observer
