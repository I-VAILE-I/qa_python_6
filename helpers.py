import datetime
import random
import allure


@allure.step(f'Генерируем случайный номер телефона')
def generate_telephone_num():
    return random.randint(80000000000, 89999999999)


def get_two_days_above(days):
    with allure.step(f'Прибавляем к сегодняшней дате {days}'):
        return (datetime.datetime.today() + datetime.timedelta(days=days)).day
