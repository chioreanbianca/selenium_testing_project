from selenium.webdriver.common.by import By

class SecureAreaPage:

    def __init__(self, driver):
        self.driver = driver

    def get_logout_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
    
    def click_logout_button(self):
        self.get_logout_button().click()

    def get_flash_message(self):
        return self.driver.find_element(By.ID, "flash")   