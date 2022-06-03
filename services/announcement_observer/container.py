"""
Announcement observer DI container.
"""
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.wiring import providers

from services.db import AsyncDatabase
from services.db.config import DB_URL


class AnnouncementObserverContainer(DeclarativeContainer):
    db = providers.Singleton(
        AsyncDatabase,
        db_url=DB_URL
    )
    cities_repository = providers.Factory(
        session_factory=db.provided.session
    )
