"""
Data access layer.
"""
from abc import ABC
from typing import Callable, AsyncContextManager

from utils.common.patterns import Repository


class SQLAlchemyRepository(Repository, ABC):
    """
    SQLAlchemy repository.
    """

    def __init__(self, session_factory: Callable[..., AsyncContextManager]):
        self.session_factory: Callable[..., AsyncContextManager] = \
            session_factory
