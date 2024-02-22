from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    # heading_by_id = [By.ID]

    def __init__(self, driver, id):
        self.driver = driver
        self.heading_id = "//div[@id='accordion__heading-0']/parent::div"
        # HomePage.heading_by_id.append(f'heading_id-{id}')

    def click_on_question_headin_by_id(self):
        WebDriverWait(self.driver, 100).until(EC.invisibility_of_element_located((By.XPATH, self.heading_id)))
        self.driver.find_element(By.XPATH, self.heading_id).click()

    def check_text_question_heading(self):
        question_heading_text = self.driver.find_element(By.ID, self.heading_id).text
        assert question_heading_text == 'Регистрация', 'Текст кнопки не равен Регистрация'
