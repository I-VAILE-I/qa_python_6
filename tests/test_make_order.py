import allure
from data import TextData, main_page_url
from helpers import generate_telephone_num
from locators.order_page_locators import OrderPageLocators, set_date
from pages.order_page import OrderPage


@allure.suite('Проверка разделов "Вопросы о важном" на главной странице в Firefox')
class TestMakeOrder:

    @allure.description('Проверяем переадресацию на оформление зазаказ, нажав кнопку "Заказать" сверху справа страницы. В конце проверяем переадресацию на главную страницу по клику на лого')
    @allure.title('Проверяем оформление заказа')
    def test_order_on_top_page(self, driver, get_two_days_above):
        check_top_page_order = OrderPage(driver=driver)
        check_top_page_order.click_to_accept_coockies(locator=OrderPageLocators.accept_coockies)
        check_top_page_order.click_on_top_order_button(locator=OrderPageLocators.order_button_top_page)
        check_top_page_order.add_name(locator=OrderPageLocators.input_name, text=TextData.name)
        check_top_page_order.add_last_name(locator=OrderPageLocators.input_last_name, text=TextData.last_name)
        check_top_page_order.add_adress(locator=OrderPageLocators.input_adress, text=TextData.adress)
        check_top_page_order.add_metro_station_sokol(locator_dropbox=OrderPageLocators.dropbox_station_metro, locator_station=OrderPageLocators.select_sokol_station)
        check_top_page_order.add_telephone_number(locator=OrderPageLocators.input_telephone_number, text=generate_telephone_num())
        check_top_page_order.next_page(locator=OrderPageLocators.next_button)
        check_top_page_order.select_two_days_above_date(locator_selection_date=OrderPageLocators.open_selection_date, locator_date=set_date(get_two_days_above))
        check_top_page_order.select_one_days_rent_period(locator_selection_date=OrderPageLocators.dropdown_rent, locator_date=OrderPageLocators.dropdown_rent_menu_one_day)
        check_top_page_order.select_black_color(locator=OrderPageLocators.checkbox_black_colors)
        check_top_page_order.add_comment_for_courier(locator=OrderPageLocators.commentation_for_courier, text=TextData.comment)
        check_top_page_order.next_page(locator=OrderPageLocators.next_button)
        check_top_page_order.click_on_button_yes(locator=OrderPageLocators.button_order_yes)
        assert check_top_page_order.check_text_question_heading(locator=OrderPageLocators.text_order_finish, text=TextData.order_text)
        check_top_page_order.go_to_order_status_page(locator=OrderPageLocators.check_order)
        check_top_page_order.go_to_main_page_by_click_on_logo(locator=OrderPageLocators.samokat_logo)
        assert check_top_page_order.check_redirrect_to_main_page(page_url=main_page_url)

    @allure.description('Проверяем переадресацию на оформление зазаказа, нажав кнопку "Заказать" по середине страницы. В конце проверяем переадресацию на главную страницу по клику на лого')
    @allure.title('Проверяем оформление заказа')
    def test_order_on_middle_page(self, driver, get_one_day_above):
        check_middle_page_order = OrderPage(driver=driver)
        check_middle_page_order.click_to_accept_coockies(locator=OrderPageLocators.accept_coockies)
        check_middle_page_order.click_on_top_order_button(locator=OrderPageLocators.order_button_top_page)
        check_middle_page_order.add_name(locator=OrderPageLocators.input_name, text=TextData.name)
        check_middle_page_order.add_last_name(locator=OrderPageLocators.input_last_name, text=TextData.last_name)
        check_middle_page_order.add_adress(locator=OrderPageLocators.input_adress, text=TextData.adress)
        check_middle_page_order.add_metro_station_salarievo(locator_dropbox=OrderPageLocators.dropbox_station_metro, locator_station=OrderPageLocators.select_salarievo_station)
        check_middle_page_order.add_telephone_number(locator=OrderPageLocators.input_telephone_number, text=generate_telephone_num())
        check_middle_page_order.next_page(locator=OrderPageLocators.next_button)
        check_middle_page_order.select_one_day_above_date(locator_selection_date=OrderPageLocators.open_selection_date, locator_date=set_date(get_one_day_above))
        check_middle_page_order.select_seven_days_rent_period(locator_selection_date=OrderPageLocators.dropdown_rent, locator_date=OrderPageLocators.dropdown_rent_menu_seven_days)
        check_middle_page_order.select_grey_color(locator=OrderPageLocators.checkbox_grey_colors)
        check_middle_page_order.add_comment_for_courier(locator=OrderPageLocators.commentation_for_courier, text=TextData.comment)
        check_middle_page_order.next_page(locator=OrderPageLocators.next_button)
        check_middle_page_order.click_on_button_yes(locator=OrderPageLocators.button_order_yes)
        assert check_middle_page_order.check_text_question_heading(locator=OrderPageLocators.text_order_finish, text=TextData.order_text)
        check_middle_page_order.go_to_order_status_page(locator=OrderPageLocators.check_order)
        check_middle_page_order.go_to_main_page_by_click_on_logo(locator=OrderPageLocators.samokat_logo)
        assert check_middle_page_order.check_redirrect_to_main_page(page_url=main_page_url)
