"""
Announcement observer Data Access Layer.
"""
from typing import List

from sqlalchemy import select

from services.amount_ads_observer.models import AdsObserver, AdsObserverStat
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


class AdsObserversStatRepository(SQLAlchemyRepository):
    """
    Advert observers statistic repository that uses SQLAlchemy.
    """
    async def select_interval(self, from_: int, to: int) -> List[AdsObserverStat]:
        """
        Returns Advert observers statistic records from timestamp interval.

        :param from_: Interval begin
        :param to: Interval end
        :return: Advert observers statistic records
        """
        async with self.session_factory() as session:
            async with session.begin():
                stmt = select(AdsObserverStat)\
                        .where(from_ <= AdsObserverStat.timestamp <= to)
                res = await session.execute(stmt)
                return res.scalars()
