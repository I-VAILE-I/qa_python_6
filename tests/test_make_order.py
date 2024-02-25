from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from pages.order_page import OrderPage


@allure.title('Проверка разделов "Вопросы о важном" на главной странице в Firefox')
class TestMakeOrder:
    driver = None
    button_allow_cookies = [By.ID, "rcc-confirm-button"]

    @classmethod
    @allure.title('Открываем браузер Firefox')
    def setup_class(cls):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--window-size=1280,720')
        cls.driver = webdriver.Firefox(options=firefox_options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru')
        cls.driver.find_element(*cls.button_allow_cookies).click()

    @allure.story('Проверяем переадресацию на оформление зазаказ, нажав кнопку сверху справа страницы')
    @allure.title('Проверяем оформление заказа')
    def test_order_on_top_page(self):
        check_top_page_order = OrderPage(driver=self.driver)
        check_top_page_order.click_on_top_order_button()
        check_top_page_order.add_name()
        check_top_page_order.add_last_name()
        check_top_page_order.add_adress()
        check_top_page_order.add_metro_station_sokol()
        check_top_page_order.add_telephone_number()
        check_top_page_order.next_page()
        check_top_page_order.select_a_27_02_24_date()
        check_top_page_order.select_one_days_rent_period()
        check_top_page_order.select_black_color()
        check_top_page_order.add_comment_for_courier()
        check_top_page_order.next_page()
        check_top_page_order.click_on_button_yes()
        check_top_page_order.check_text_question_heading()
        check_top_page_order.go_to_order_status_page()
        check_top_page_order.go_to_main_page_by_click_on_logo()

    @allure.story('Проверяем переадресацию на оформление зазаказ, нажав кнопку "Заказать" по среедине страницы')
    @allure.title('Проверяем оформление заказа')
    def test_order_on_middle_page(self):
        check_middle_page_order = OrderPage(driver=self.driver)
        check_middle_page_order.click_on_top_order_button()
        check_middle_page_order.add_name()
        check_middle_page_order.add_last_name()
        check_middle_page_order.add_adress()
        check_middle_page_order.add_metro_station_salarievo()
        check_middle_page_order.add_telephone_number()
        check_middle_page_order.next_page()
        check_middle_page_order.select_a_29_02_24_date()
        check_middle_page_order.select_seven_days_rent_period()
        check_middle_page_order.select_grey_color()
        check_middle_page_order.add_comment_for_courier()
        check_middle_page_order.next_page()
        check_middle_page_order.click_on_button_yes()
        check_middle_page_order.check_text_question_heading()
        check_middle_page_order.go_to_order_status_page()
        check_middle_page_order.go_to_main_page_by_click_on_logo()

    @classmethod
    @allure.title('Закрываем браузер')
    def teardown_class(cls):
        cls.driver.quit()
