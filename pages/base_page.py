import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.suite('Проверка разделов "Вопросы о важном" на главной странице в Firefox')
class BasePage:

    def __int__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    def input_text_in_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def open_new_tab(self, title):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(title))

    def get_current_urls(self):
        return self.driver.current_url
