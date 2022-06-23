"""
Private Avito API executor service.
"""
import urllib
from typing import Optional

from playwright.async_api import Playwright, Browser, Page

from services.private_avito_api_executor.private_avito_api_executor_pb2 import GetAmountAdsResponse,\
    GetAmountAdsRequest
from services.private_avito_api_executor.private_avito_api_executor_pb2_grpc import PrivateAvitoApiExecutorServicer
from services.private_avito_api_executor.schemas.items import AvitoItemsResponse
from utils.playwright.request import make_async_get_request


class AsyncPrivateAvitoApiExecutorService(
    PrivateAvitoApiExecutorServicer
):
    def __init__(self, playwright: Playwright):
        super().__init__()

        self.playwright = playwright
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None

    async def get_amount_ads(
        self, request: GetAmountAdsRequest, context
    ) -> GetAmountAdsResponse:
        params = {
            'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
            'locationId': str(request.location_id),
            'query': request.query,
            'countOnly': '1',
        }
        url = 'https://m.avito.ru/api/11/items?'
        url += urllib.parse.urlencode(params)
        response = await make_async_get_request(self.page, url, AvitoItemsResponse)
        return GetAmountAdsResponse(amount=response.result.count)

    async def run_browser(self):
        self.browser = await self.playwright.chromium.launch()
        self.page = await self.browser.new_page()
        return self

    async def finalize(self):
        await self.browser.close()
