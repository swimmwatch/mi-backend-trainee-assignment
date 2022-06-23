"""
Announcement observer DI container.
"""
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.wiring import providers

from services.amount_ads_observer.dal import AdObserversRepository
from services.db import AsyncDatabase
from services.db.config import DB_URL


class AmountAdsObserverContainer(DeclarativeContainer):
    db = providers.Singleton(
        AsyncDatabase,
        db_url=DB_URL
    )
    ad_observers_repository = providers.Factory(
        AdObserversRepository,
        session_factory=db.provided.session
    )
