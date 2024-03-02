import allure
import pytest
from selenium import webdriver
from pages.main_page import HomePage


@allure.suite('Проверка разделов "Вопросы о важном" на главной странице в Firefox')
class TestMainPageHeadings:
    driver = None

    @classmethod
    def setup_class(cls):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--window-size=1280,720')
        cls.driver = webdriver.Firefox(options=firefox_options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru')

    @pytest.mark.parametrize("id", [i for i in range(0, 8)])
    @allure.title(f'Проверяем {id} вопрос')
    @allure.description('Проверяем ответы на вопросы')
    def test_check_heading_text(
            self,
            id: int
    ):
        check_question_sections = HomePage(driver=self.driver)
        if id == 0:
            check_question_sections.click_to_accept_coockies()
        check_question_sections.click_on_question_headin_by_id(id=id)
        check_question_sections.check_text_question_heading(id=id)

    @classmethod
    @allure.title('Заркываем браузер')
    def teardown_class(cls):
        cls.driver.quit()
