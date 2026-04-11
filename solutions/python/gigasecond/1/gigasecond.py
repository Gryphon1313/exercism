from datetime import datetime, timedelta


def add(moment: datetime) -> datetime:
    gigasecond = 10**9
    return moment + timedelta(seconds=gigasecond)
