import calendar
from datetime import datetime


def get_uts_from_datatime(dt: datetime) -> int:
    """
    Convert datetime object into unix timestamp.

    :param dt: datatime instance
    :return: Unix timestamp
    """
    current_datetime = dt.utcnow()
    current_timetuple = current_datetime.utctimetuple()
    return calendar.timegm(current_timetuple)
