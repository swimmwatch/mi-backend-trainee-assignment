"""
Adverts observer statistic schemas.
"""
from pydantic import BaseModel


class BaseAdsObserverStat(BaseModel):
    amount: int
    timestamp: str
    ads_observer_id: int


class AdsObserverStatCreate(BaseAdsObserverStat):
    pass


class AdsObserverStat(BaseAdsObserverStat):
    id: int

    class Config:
        orm_mode = True
