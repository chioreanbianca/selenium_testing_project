from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class TestBase:
    def setup_method(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()


    def teardown_method(self):
        if self.driver:
            self.driver.quit()
