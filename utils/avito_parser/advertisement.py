"""
Avito advertisement parser utils.
"""
import asyncio

import httpx
from bs4 import BeautifulSoup
from fake_headers import Headers


async def get_amount_advertisements(query: str, location_id: int) -> int:
    """
    Get amount advertisements by searching query and location ID.

    :param query: Searching query
    :param location_id: Avito location ID
    :return: Amount advertisements
    """
    headers = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )
    async with httpx.AsyncClient(headers=headers.generate()) as client:
        data = {
            'locationId': location_id,
            'name': query,
            'cd': 0,
            's': 101
        }
        response = await client.post(
            'https://www.avito.ru/search',
            follow_redirects=True,
            data=data
        )
        # TODO: remove hard coded HTTP status
        if response.status_code == 404:
            raise ValueError(f'No such location id: {location_id}')

        soup = BeautifulSoup(response.text, 'html.parser')
        amount_el = soup.select_one('[data-marker="page-title/count"]')
        # TODO: handle if amount element was not found
        only_digits = ''.join(filter(lambda ch: ch.isdigit(), amount_el.text))
        amount = int(only_digits)
        return amount


async def main():
    amount = await get_amount_advertisements('ps5', 653140)
    print(amount)


if __name__ == '__main__':
    asyncio.run(main())
