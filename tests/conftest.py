import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1280,720')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru')
    yield driver
    driver.quit()
