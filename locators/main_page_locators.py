import allure
from selenium.webdriver.common.by import By


class MainPageLocators:
    COOCKIES_ALLOW = [By.ID, "rcc-confirm-button"]


@allure.step('Выставляем айди вопроса')
def get_heading_locator_with_id(id: int):
    return [By.ID, f"accordion__heading-{id}"]


@allure.step('Выставляем айди блока текста')
def get_accordion_locator_with_id(id: int):
    return [By.ID, f"accordion__panel-{id}"]