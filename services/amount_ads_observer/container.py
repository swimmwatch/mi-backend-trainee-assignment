"""
Announcement observer DI container.
"""
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.wiring import providers

from services.amount_ads_observer.dal import AdsObserversRepository
from services.db import AsyncDatabase
from services.db.config import database_settings


class AmountAdsObserverContainer(DeclarativeContainer):
    db = providers.Singleton(
        AsyncDatabase,
        db_url=database_settings.db_url
    )
    ads_observers_repository = providers.Factory(
        AdsObserversRepository,
        session_factory=db.provided.session
    )
