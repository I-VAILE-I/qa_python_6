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

    def __init__(self, driver, id: int):
        self.driver = driver
        self.heading_id = [By.ID, f"accordion__heading-{id}"]
        self.accordion_id = [By.ID, f"accordion__panel-{id}"]

    @allure.step('Кликаем на вопрос')
    def click_on_question_headin_by_id(self):
        self.driver.find_element(*self.heading_id).click()

    @allure.step('Проверяем ответ на вопрос')
    @allure.description('Проверяем ответ на вопрос')
    def check_text_question_heading(self):
        question_heading_text = self.driver.find_element(*self.accordion_id).text
        id = self.heading_id[1][-1]
        assert question_heading_text == self.lst_expected_texts[int(id)]

