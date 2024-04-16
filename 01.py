from datetime import datetime


def get_days_from_today(date: str) -> int:
    return (datetime.today() - datetime.fromisoformat(date)).days


print(get_days_from_today("2021-10-09"))