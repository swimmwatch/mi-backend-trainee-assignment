"""
Avito items schemas
"""
from pydantic import BaseModel, Field

from services.private_avito_api_executor.schemas.base import AvitoBaseResponse


class AvitoItemsInfo(BaseModel):
    count: int
    total_count: int = Field(alias='totalCount')
    main_count: int = Field(alias='mainCount')


class AvitoItemsResponse(AvitoBaseResponse):
    result: AvitoItemsInfo
