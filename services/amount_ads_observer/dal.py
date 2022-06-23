"""
Announcement observer Data Access Layer.
"""
from typing import List

from sqlalchemy.future import select

from services.amount_ads_observer.models import City
from utils.sqlalchemy.dal import SQLAlchemyRepository


class AdObserversRepository(SQLAlchemyRepository):
    """
    Advert observers repository that uses SQLAlchemy.
    """
    async def get_all(self) -> List[City]:
        async with self.session_factory() as session:
            async with session.begin():
                stmt = select(City)
                res = await session.execute(stmt)
                return res.scalars().all()
