"""
Announcement observer database models.
"""
from sqlalchemy import Column, Integer, String

from services.db import Base


class AdObserver(Base):
    __tablename__ = 'ad_observers'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, nullable=False)
    query = Column(String, nullable=False)
