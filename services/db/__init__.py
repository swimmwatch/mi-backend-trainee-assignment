"""
Database service.
"""
from contextlib import asynccontextmanager

from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from services.db.protocols import SQLAlchemyDatabaseProtocol
from services.db.types import SessionType

Base = declarative_base()


class AsyncDatabase(SQLAlchemyDatabaseProtocol):
    def __init__(self, db_url: str):
        """
        :param db_url: Database URL.
        """
        self._engine = create_async_engine(db_url, echo=True)
        self._session_factory = sessionmaker(
            self._engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    @asynccontextmanager
    async def session(self):
        session: AsyncSession = self._session_factory()
        try:
            yield session
        except Exception as err:
            logger.error(f'Session rollback because of exception: {err}')
            await session.rollback()
        finally:
            await session.close()

    async def init(self):
        """
        Database initialization.
        """
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
