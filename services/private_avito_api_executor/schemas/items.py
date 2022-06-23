"""
Avito items schemas
"""
from enum import Enum

from pydantic import BaseModel, Field

from services.private_avito_api_executor.schemas.base import BaseAvitoResponse


class AvitoItemsInfo(BaseModel):
    count: int
    total_count: int = Field(alias='totalCount')
    main_count: int = Field(alias='mainCount')


class AvitoItemsResponse(BaseAvitoResponse):
    result: AvitoItemsInfo


class AvitoItemsCountState(Enum):
    TRUE = 1
    FALSE = 0


class AvitoItemsRequest(BaseModel):
    key: str
    location_id: int = Field(alias='locationId')
    query: str
    count_only: AvitoItemsCountState = AvitoItemsCountState.TRUE
