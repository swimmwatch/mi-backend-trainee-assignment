"""
Announcement observer Data Access Layer.
"""
from typing import List

from sqlalchemy.future import select

from services.announcement_observer.models import City
from utils.sqlalchemy.dal import SQLAlchemyRepository


class CityRepository(SQLAlchemyRepository):
    """
    City repository that uses SQLAlchemy.
    """
    async def get_all(self) -> List[City]:
        async with self.session_factory() as session:
            async with session.begin():
                stmt = select(City)
                res = await session.execute(stmt)
                return res.scalars().all()
