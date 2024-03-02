import allure
from selenium.webdriver.common.by import By


class HomePage:
    lst_expected_texts = [
        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
     ]
    button_allow_cookies = [By.ID, "rcc-confirm-button"]
    heading_id = [By.ID, f"accordion__heading-{id}"]
    accordion_id = [By.ID, f"accordion__panel-{id}"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выставляем айди вопроса')
    def set_heading_id(self, id: int):
        self.heading_id = [By.ID, f"accordion__heading-{id}"]

    @allure.step('Выставляем айди блока текста')
    def set_accordion_id(self, id: int):
        self.accordion_id = [By.ID, f"accordion__panel-{id}"]

    @allure.step('Соглашаемся с использованием coockies')
    def click_to_accept_coockies(self):
        self.driver.find_element(*self.button_allow_cookies).click()

    @allure.step('Кликаем на вопрос')
    def click_on_question_headin_by_id(self, id: int):
        self.set_heading_id(id=id)
        self.driver.find_element(*self.heading_id).click()

    @allure.step('Проверяем ответ на вопрос')
    @allure.description('Проверяем ответ на вопрос')
    def check_text_question_heading(self, id: int):
        self.set_accordion_id(id=id)
        question_heading_text = self.driver.find_element(*self.accordion_id).text
        assert question_heading_text == self.lst_expected_texts[id]

