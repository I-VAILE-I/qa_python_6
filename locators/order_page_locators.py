from selenium.webdriver.common.by import By


class OrderPageLocators:
    accept_coockies = [By.ID, "rcc-confirm-button"]
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


def set_date(date: int):
    return [By.XPATH, f"//*[text() = '{date}']"]

