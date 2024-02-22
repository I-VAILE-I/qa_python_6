import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()  # создали объект для опций
    firefox_options.add_argument('--window-size=1280,720')  # добавили ещё настройку
    driver = webdriver.Firefox(options=firefox_options)  # создали драйвер и передали в него настройки
    driver.get('https://qa-scooter.praktikum-services.ru')
    yield driver
    driver.quit()
