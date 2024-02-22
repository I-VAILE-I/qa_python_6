import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object.HomePage import HomePage


class TestMainPageHeadings:
    driver = None

    @classmethod
    def setup_class(cls):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--window-size=1280,720')
        cls.driver = webdriver.Firefox(options=firefox_options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru')

    @pytest.mark.parametrize("id", [i for i in range(0, 8)])
    def test_check_email_placeholder(
            self,
            id: int
    ):
        check_question_sections = HomePage(driver=self.driver, id=id)
        check_question_sections.click_on_question_headin_by_id()
        check_question_sections.check_text_question_heading()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
