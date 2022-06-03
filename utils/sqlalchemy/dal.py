"""
Data access layer.
"""
from abc import ABC
from typing import Generic, Callable

from utils.common.patterns import Repository
from utils.common.types import ContextManagerType


class SQLAlchemyRepository(Repository, ABC, Generic[ContextManagerType]):
    """
    SQLAlchemy repository.
    """

    def __init__(self, session_factory: Callable[..., ContextManagerType]):
        self.session_factory: Callable[..., ContextManagerType] = session_factory
