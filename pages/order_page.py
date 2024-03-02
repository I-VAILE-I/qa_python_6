import datetime

import allure
from selenium.webdriver.common.by import By

from helpers import generate_telephone_num


class OrderPage:
    order_button_top_page = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    order_button_middle_page = [By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']"]
    input_name = [By.XPATH, "//input[@placeholder='* Имя']"]
    input_last_name = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    input_adress = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    dropbox_station_metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    select_sokol_station = [By.XPATH, "//*[text() = 'Сокол']"]
    select_salarievo_station = [By.XPATH, "//*[text() = 'Саларьево']"]
    input_telephone_number = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    open_selection_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    select_27_02_24_date = [By.XPATH, "//*[text() = '27']"]
    select_date = []
    dropdown_rent = [By.XPATH, "//div[@class='Dropdown-control']"]
    dropdown_rent_menu_one_day = [By.XPATH, "//*[text() = 'сутки']"]
    dropdown_rent_menu_seven_days = [By.XPATH, "//*[text() = 'семеро суток']"]
    checkbox_black_colors = [By.XPATH, "//label[@for='black']"]
    checkbox_grey_colors = [By.XPATH, "//label[@for='grey']"]
    commentation_for_courier = [By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    button_order_yes = [By.XPATH, "//*[text() = 'Да']"]
    text_order_finish = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]
    check_order = [By.XPATH, "//*[text() = 'Посмотреть статус']"]
    samokat_logo = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]

    def __init__(self, driver):
        self.driver = driver

    def set_date(self, date: int):
        self.select_date = [By.XPATH, f"//*[text() = '{date}']"]

    @allure.step('Кликаем на кнопку "Заказать" сверху справа страницы')
    def click_on_top_order_button(self):
        self.driver.find_element(*self.order_button_top_page).click()

    @allure.step('Кликаем на кнопку "Заказать" по середине страницы')
    def click_on_middle_order_button(self):
        self.driver.find_element(*self.order_button_middle_page).click()

    @allure.step('Вписываем имя в заказ')
    def add_name(self):
        self.driver.find_element(*self.input_name).send_keys('Андрей')

    @allure.step('Вписываем фамилию в заказ')
    def add_last_name(self):
        self.driver.find_element(*self.input_last_name).send_keys('Анченко')

    @allure.step('Вписываем адрес в заказ')
    def add_adress(self):
        self.driver.find_element(*self.input_adress).send_keys('Дом колотушкина')

    @allure.step('Выбираем метро "Сокол" из выпадающего списка')
    def add_metro_station_sokol(self):
        self.driver.find_element(*self.dropbox_station_metro).click()
        self.driver.find_element(*self.select_sokol_station).click()

    @allure.step('Выбираем метро "Саларьево" из выпадающего списка')
    def add_metro_station_salarievo(self):
        self.driver.find_element(*self.dropbox_station_metro).click()
        self.driver.find_element(*self.select_salarievo_station).click()

    @allure.step('Вписываем телефонный номер')
    def add_telephone_number(self):
        self.driver.find_element(*self.input_telephone_number).send_keys(generate_telephone_num())

    @allure.step('Переходим на следующую страницу')
    def next_page(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step(f'Прибавляем к сегодняшней дате 1 или 2 дня')
    def get_two_days_above(self, days_above: int):
        return (datetime.datetime.today() + datetime.timedelta(days=days_above)).day

    @allure.step('Выбираем дату +1 дня')
    def select_one_day_above_date(self):
        self.driver.find_element(*self.open_selection_date).click()
        self.set_date(date=self.get_two_days_above(days_above=1))
        self.driver.find_element(*self.select_date).click()

    @allure.step('Выбираем дату +2 дня')
    def select_two_days_above_date(self):
        self.driver.find_element(*self.open_selection_date).click()
        self.set_date(date=self.get_two_days_above(days_above=2))
        self.driver.find_element(*self.select_date).click()

    @allure.step('Выбираем суточную аренду')
    def select_one_days_rent_period(self):
        self.driver.find_element(*self.dropdown_rent).click()
        self.driver.find_element(*self.dropdown_rent_menu_one_day).click()

    @allure.step('Выбираем семидневную аренду')
    def select_seven_days_rent_period(self):
        self.driver.find_element(*self.dropdown_rent).click()
        self.driver.find_element(*self.dropdown_rent_menu_seven_days).click()

    @allure.step('Выбираем черный цвет самоката')
    def select_black_color(self):
        self.driver.find_element(*self.checkbox_black_colors).click()

    @allure.step('Выбираем серый цвет самоката')
    def select_grey_color(self):
        self.driver.find_element(*self.checkbox_grey_colors).click()

    @allure.step('Вписываем комментарий курьеру')
    def add_comment_for_courier(self):
        self.driver.find_element(*self.commentation_for_courier).send_keys('Жду на остановке :]')

    @allure.step('Соглашаемся с условиями и нажимаем на "Да"')
    def click_on_button_yes(self):
        self.driver.find_element(*self.button_order_yes).click()

    @allure.step('Кликаем на кнопку "Посмотреть статус"')
    def go_to_order_status_page(self):
        self.driver.find_element(*self.check_order).click()

    @allure.step('Нажимаем на логотип для "Самокат" для перехода на главную страницу')
    def go_to_main_page_by_click_on_logo(self):
        self.driver.find_element(*self.samokat_logo).click()

    @allure.step('Проверяем, что окно статуса имеет текст "Заказ оформлен"')
    def check_text_question_heading(self):
        order_text = self.driver.find_element(*self.text_order_finish).text[0:14]
        assert order_text == 'Заказ оформлен'

    @allure.step('Проверяем, что переходить на главную страницу')
    def check_redirrect_to_main_page(self):
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

