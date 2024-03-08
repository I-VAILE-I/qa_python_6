import allure
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Соглашаемся с использованием coockies')
    def click_to_accept_coockies(self, locator):
        self.click_on_element(locator)

    @allure.step('Кликаем на кнопку "Заказать" сверху справа страницы')
    def click_on_top_order_button(self, locator):
        self.click_on_element(locator)

    @allure.step('Кликаем на кнопку "Заказать" по середине страницы')
    def click_on_middle_order_button(self, locator):
        self.click_on_element(locator)

    @allure.step('Вписываем имя в заказ')
    def add_name(self, locator, text):
        self.input_text_in_field(locator, text)

    @allure.step('Вписываем фамилию в заказ')
    def add_last_name(self, locator, text):
        self.input_text_in_field(locator, text)

    @allure.step('Вписываем адрес в заказ')
    def add_adress(self, locator, text):
        self.input_text_in_field(locator, text)

    @allure.step('Выбираем метро "Сокол" из выпадающего списка')
    def add_metro_station_sokol(self, locator_dropbox, locator_station):
        self.click_on_element(locator_dropbox)
        self.click_on_element(locator_station)

    @allure.step('Выбираем метро "Саларьево" из выпадающего списка')
    def add_metro_station_salarievo(self, locator_dropbox, locator_station):
        self.click_on_element(locator_dropbox)
        self.click_on_element(locator_station)

    @allure.step('Вписываем телефонный номер')
    def add_telephone_number(self, locator, text):
        self.input_text_in_field(locator, text)

    @allure.step('Переходим на следующую страницу')
    def next_page(self, locator):
        self.click_on_element(locator)

    @allure.step('Выбираем дату +1 дня')
    def select_one_day_above_date(self, locator_selection_date, locator_date):
        self.click_on_element(locator_selection_date)
        self.click_on_element(locator_date)

    @allure.step('Выбираем дату +2 дня')
    def select_two_days_above_date(self, locator_selection_date, locator_date):
        self.click_on_element(locator_selection_date)
        self.click_on_element(locator_date)

    @allure.step('Выбираем суточную аренду')
    def select_one_days_rent_period(self, locator_selection_date, locator_date):
        self.click_on_element(locator_selection_date)
        self.click_on_element(locator_date)

    @allure.step('Выбираем семидневную аренду')
    def select_seven_days_rent_period(self, locator_selection_date, locator_date):
        self.click_on_element(locator_selection_date)
        self.click_on_element(locator_date)

    @allure.step('Выбираем черный цвет самоката')
    def select_black_color(self, locator):
        self.click_on_element(locator)

    @allure.step('Выбираем серый цвет самоката')
    def select_grey_color(self, locator):
        self.click_on_element(locator)

    @allure.step('Вписываем комментарий курьеру')
    def add_comment_for_courier(self, locator, text):
        self.input_text_in_field(locator, text)

    @allure.step('Соглашаемся с условиями и нажимаем на "Да"')
    def click_on_button_yes(self, locator):
        self.click_on_element(locator)

    @allure.step('Кликаем на кнопку "Посмотреть статус"')
    def go_to_order_status_page(self, locator):
        self.click_on_element(locator)

    @allure.step('Нажимаем на логотип для "Самокат" для перехода на главную страницу')
    def go_to_main_page_by_click_on_logo(self, locator):
        self.click_on_element(locator)

    @allure.step('Проверяем, что окно статуса имеет текст "Заказ оформлен"')
    def check_text_question_heading(self, locator, text):
        return self.get_text_element(locator)[0:14] == text

    @allure.step('Проверяем, что переходить на главную страницу')
    def check_redirrect_to_main_page(self, page_url):
        return self.get_current_urls() == page_url
