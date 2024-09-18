from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
    
    def get_username_element(self):
        return self.driver.find_element(By.ID, "username")

    def get_password_element(self):
        return self.driver.find_element(By.ID, "password")

    def get_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    def get_flash_message(self):
        return self.driver.find_element(By.ID, "flash")

    def set_username(self, username):
        username_field = self.get_username_element()
        username_field.clear()
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.get_password_element()
        password_field.clear()  
        password_field.send_keys(password)

    def click_login(self):
        self.get_login_button().click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
