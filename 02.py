import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    tickets = set()
    while len(tickets) < quantity:
        tickets.add(random.randint(min, max))
    return sorted(tickets)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
