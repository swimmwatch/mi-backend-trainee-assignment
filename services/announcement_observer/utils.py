"""
Announcement observer utils.
"""
from services.announcement_observer.models import City
from services.db import AsyncDatabase


async def async_init_db(db: AsyncDatabase):
    """
    Init database.
    :param db: Database
    """

    await db.init()

    async with db.session() as session:
        # init subjects
        session.add_all(
            City(name=name) for name in [
                'Moscow',
                'New York',
                'Sydney'
            ]
        )

        await session.commit()
