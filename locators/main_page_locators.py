import allure
from selenium.webdriver.common.by import By


class MainPageLocators:
    COOCKIES_ALLOW = [By.ID, "rcc-confirm-button"]


def get_heading_locator_with_id(id: int):
    with allure.step(f'Проверяем вопрос под номером - {id}'):
        return [By.ID, f"accordion__heading-{id}"]


def get_accordion_locator_with_id(id: int):
    with allure.step(f'Проверяем ответ под номером - {id}'):
        return [By.ID, f"accordion__panel-{id}"]
