from random import randint


def get_rates(buy, sell, location, amount):
    return print(f"Отдаю {sell}, получаю {buy}, город {location} колличество {amount}. Rate: {randint(1, 10)}")
