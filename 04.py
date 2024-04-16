from datetime import datetime


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today_date = datetime.now()
    for user in users:
        user_date = datetime.strptime(user["birthday"], "%Y.%m.%d").replace(year=today_date.year)
        if user_date.date() < today_date.date():
            user_date = user_date.replace(year=user_date.year+1)
        if user_date.weekday() == 5:
            user_date = user_date.replace(day=user_date.day+2)
        if user_date.weekday() == 6:
            user_date = user_date.replace(day=user_date.day+1)
        delta_date = user_date.date() - today_date.date()
        if delta_date.days <= 7:
            user['congratulation_date'] = user_date.strftime("%Y.%m.%d")
            user.pop('birthday')
    return [user for user in users if 'congratulation_date' in user]


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
