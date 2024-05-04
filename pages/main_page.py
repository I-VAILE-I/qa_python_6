import allure
from locators.main_page_locators import MainPageLocators, get_heading_locator_with_id, get_accordion_locator_with_id
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Соглашаемся с использованием coockies')
    def click_to_accept_coockies(self):
        self.click_on_element(locator=MainPageLocators.COOCKIES_ALLOW)

    @allure.step('Кликаем на вопрос')
    def click_on_question_headin_by_id(self, id):
        self.click_on_element(get_heading_locator_with_id(id=id))

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_on_question_headin_by_id(self, id):
        return self.get_text_element(get_accordion_locator_with_id(id=id))

    @allure.step('Проверяем ответ на вопрос')
    def check_text_question_heading(self, question_text, expected_text):
        return question_text == expected_text

