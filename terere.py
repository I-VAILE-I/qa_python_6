from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__ == '__main__':
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1280,720')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru')

    # WebDriverWait(driver, 100).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='accordion__heading-0']/parent::div")))
    driver.find_element(By.XPATH, "//button[@id='rcc-confirm-button']").click()
    driver.get_cookies()
    driver.find_element(By.XPATH, "//*[@id='accordion__heading-0']").click()
    driver.find_element(By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']").click()
