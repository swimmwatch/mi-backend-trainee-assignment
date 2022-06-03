"""
Announcement observer Data Access Layer.
"""
from typing import AsyncContextManager, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from services.announcement_observer.models import City
from utils.sqlalchemy.dal import SQLAlchemyRepository


class CityRepository(SQLAlchemyRepository[AsyncContextManager[AsyncSession]]):
    """
    City repository that uses SQLAlchemy.
    """
    async def get_all(self) -> List[City]:
        async with self.session_factory() as session:
            async with session.begin():
                stmt = select(City)
                res = await session.execute(stmt)
                return res.scalars()
