"""
Avito items schemas
"""
from pydantic import BaseModel

from services.private_avito_api_executor.schemas.base import AvitoBaseResponse


class AvitoItemsInfo(BaseModel):
    count: int
    total_count: int
    main_count: int


class AvitoItemsResponse(AvitoBaseResponse):
    result: AvitoItemsInfo
