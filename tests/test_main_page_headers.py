import allure
import pytest
from data import lst_expected_texts
from pages.main_page import HomePage


@allure.suite('Проверка разделов "Вопросы о важном" на главной странице в Firefox')
class TestMainPageHeadings:

    @pytest.mark.parametrize("id", [i for i in range(0, 8)])
    @allure.title(f'Проверяем {id} вопрос')
    @allure.description('Проверяем ответы на вопросы')
    def test_check_heading_text(
            self,
            driver,
            id: int,
    ):
        home_page = HomePage(driver=driver)
        home_page.click_to_accept_coockies()
        home_page.click_on_question_headin_by_id(id=id)
        answer_text = home_page.get_answer_on_question_headin_by_id(id=id)
        assert home_page.check_text_question_heading(question_text=answer_text, expected_text=lst_expected_texts[id])
