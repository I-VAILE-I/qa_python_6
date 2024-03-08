import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from pages.order_page import OrderPage


@pytest.fixture(scope="function")
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1280,720')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru')
    yield driver
    driver.quit()


@allure.step(f'Прибавляем к сегодняшней дате 2 дня')
@pytest.fixture(scope="function")
def get_two_days_above():
    return (datetime.datetime.today() + datetime.timedelta(days=2)).day


@allure.step(f'Прибавляем к сегодняшней дате 1 день')
@pytest.fixture(scope="function")
def get_one_day_above():
    return (datetime.datetime.today() + datetime.timedelta(days=2)).day
