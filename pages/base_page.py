import allure


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

    def get_current_urls(self):
        return self.driver.current_url
