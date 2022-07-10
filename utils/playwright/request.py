"""
Playwright request utils.
"""
from typing import Type, TypeVar

from playwright.async_api import Page
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)


async def make_async_get_request(page: Page, url: str, schema_type: Type[T]) -> T:
    """
    Make GET request by Playwright.

    :param schema_type: Pydantic schema
    :param page: Playwright page
    :param url: URL
    :return: Schema instance
    """
    response = await page.goto(url, wait_until='load')
    content = await response.body()
    return schema_type.parse_raw(content)
