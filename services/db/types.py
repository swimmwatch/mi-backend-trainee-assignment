"""
Custom typings for DB package.
"""
from typing import TypeVar, Union, ContextManager, AsyncContextManager

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

SessionType = TypeVar('SessionType', AsyncSession, Session)
AnySessionAbstractContextManager = Union[ContextManager[SessionType], AsyncContextManager[SessionType]]
