"""
Adverts observer statistic schemas.
"""
from pydantic import BaseModel


class BaseAdsObserverStat(BaseModel):
    amount: int
    timestamp: str


class AdsObserverStatCreate(BaseAdsObserverStat):
    pass


class AdsObserverStat(BaseAdsObserverStat):
    id: int

    class Config:
        orm_mode = True
