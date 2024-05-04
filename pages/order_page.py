import allure
from data import TextData, main_page_url, dzen_page_url
from helpers import get_two_days_above, generate_telephone_num
from locators.order_page_locators import OrderPageLocators, set_date
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Соглашаемся с использованием coockies')
    def click_to_accept_coockies(self):
        self.click_on_element(locator=OrderPageLocators.accept_coockies)

    @allure.step('Кликаем на кнопку "Заказать" сверху справа страницы')
    def click_on_top_order_button(self):
        self.click_on_element(locator=OrderPageLocators.order_button_top_page)

    @allure.step('Кликаем на кнопку "Заказать" по середине страницы')
    def click_on_middle_order_button(self, locator):
        self.click_on_element(locator)

    @allure.step('Вписываем имя в заказ')
    def add_name(self):
        self.input_text_in_field(locator=OrderPageLocators.input_name,  text=TextData.name)

    @allure.step('Вписываем фамилию в заказ')
    def add_last_name(self):
        self.input_text_in_field(locator=OrderPageLocators.input_last_name, text=TextData.last_name)

    @allure.step('Вписываем адрес в заказ')
    def add_adress(self):
        self.input_text_in_field(locator=OrderPageLocators.input_adress, text=TextData.adress)

    @allure.step('Выбираем метро "Сокол" из выпадающего списка')
    def add_metro_station_sokol(self):
        self.click_on_element(locator=OrderPageLocators.dropbox_station_metro)
        self.click_on_element(locator=OrderPageLocators.select_sokol_station)

    @allure.step('Выбираем метро "Саларьево" из выпадающего списка')
    def add_metro_station_salarievo(self):
        self.click_on_element(locator=OrderPageLocators.dropbox_station_metro)
        self.click_on_element(locator=OrderPageLocators.select_salarievo_station)

    @allure.step('Вписываем телефонный номер')
    def add_telephone_number(self):
        self.input_text_in_field(locator=OrderPageLocators.input_telephone_number, text=generate_telephone_num())

    @allure.step('Переходим на следующую страницу')
    def next_page(self):
        self.click_on_element(locator=OrderPageLocators.next_button)

    @allure.step('Выбираем дату +1 дня')
    def select_one_day_above_date(self):
        self.click_on_element(locator=OrderPageLocators.open_selection_date)
        self.click_on_element(locator=set_date(get_two_days_above(days=1)))

    @allure.step('Выбираем дату +2 дня')
    def select_two_days_above_date(self):
        self.click_on_element(locator=OrderPageLocators.open_selection_date)
        self.click_on_element(locator=set_date(get_two_days_above(days=2)))

    @allure.step('Выбираем суточную аренду')
    def select_one_days_rent_period(self):
        self.click_on_element(locator=OrderPageLocators.dropdown_rent)
        self.click_on_element(locator=OrderPageLocators.dropdown_rent_menu_one_day)

    @allure.step('Выбираем семидневную аренду')
    def select_seven_days_rent_period(self):
        self.click_on_element(locator=OrderPageLocators.dropdown_rent)
        self.click_on_element(locator=OrderPageLocators.dropdown_rent_menu_seven_days)

    @allure.step('Выбираем черный цвет самоката')
    def select_black_color(self):
        self.click_on_element(locator=OrderPageLocators.checkbox_black_colors)

    @allure.step('Выбираем серый цвет самоката')
    def select_grey_color(self):
        self.click_on_element(locator=OrderPageLocators.checkbox_grey_colors)

    @allure.step('Вписываем комментарий курьеру')
    def add_comment_for_courier(self):
        self.input_text_in_field(locator=OrderPageLocators.commentation_for_courier, text=TextData.comment)

    @allure.step('Соглашаемся с условиями и нажимаем на "Да"')
    def click_on_button_yes(self):
        self.click_on_element(locator=OrderPageLocators.button_order_yes)

    @allure.step('Кликаем на кнопку "Посмотреть статус"')
    def go_to_order_status_page(self):
        self.click_on_element(locator=OrderPageLocators.check_order)

    @allure.step('Нажимаем на логотип для "Самокат" для перехода на главную страницу')
    def go_to_main_page_by_click_on_logo(self):
        self.click_on_element(locator=OrderPageLocators.samokat_logo)

    @allure.step('Нажимаем на логотип для "Яндекс" для перехода на главную страницу')
    def go_to_dzen_page_by_click_on_logo(self):
        self.click_on_element(locator=OrderPageLocators.yandex_logo)

    @allure.step('Проверяем, что окно статуса имеет текст "Заказ оформлен"')
    def check_text_question_heading(self):
        return self.get_text_element(locator=OrderPageLocators.text_order_finish)[0:14] ==  TextData.order_text

    @allure.step('Проверяем, что переходит на главную страницу')
    def check_redirrect_to_main_page(self):
        return self.get_current_urls() == main_page_url

    @allure.step('Проверяем, что переходит на новую вкладку Дзена')
    def check_redirrect_to_dzen_page(self):
        self.open_new_tab(title=dzen_page_url)
        return self.get_current_urls() == dzen_page_url
