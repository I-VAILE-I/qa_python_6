import allure
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Соглашаемся с использованием coockies')
    def click_to_accept_coockies(self, locator):
        self.click_on_element(locator)

    @allure.step('Кликаем на вопрос')
    def click_on_question_headin_by_id(self, locator):
        self.click_on_element(locator)

    @allure.step('Кликаем на вопрос')
    def get_answer_on_question_headin_by_id(self, locator):
        return self.get_text_element(locator)

    @allure.step('Проверяем ответ на вопрос')
    def check_text_question_heading(self, question_text, expected_text):
        return question_text == expected_text

