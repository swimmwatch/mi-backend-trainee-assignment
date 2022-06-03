"""
Database protocols.
"""
from typing import Protocol

from utils.sqlalchemy.types import AnySessionAbstractContextManager


class SQLAlchemyDatabaseProtocol(Protocol):
    """
    SQLAlchemy database protocol.
    """
    def session(self) -> AnySessionAbstractContextManager:
        """
        Implements method that returns SQLAlchemy session context manager.
        """
        ...

    def init(self):
        """
        Implements initialization.
        """
        ...
