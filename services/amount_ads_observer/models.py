"""
Announcement observer database models.
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from services.db import Base


class AdsObserver(Base):
    __tablename__ = 'ads_observers'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, nullable=False)
    query = Column(String, nullable=False)


class AdsObserverStat(Base):
    __tablename__ = 'ads_observer_stats'

    id = Column(Integer, primary_key=True)
    ad_observer_id = Column(Integer, ForeignKey('ads_observers.id'), nullable=False)
    timestamp = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
