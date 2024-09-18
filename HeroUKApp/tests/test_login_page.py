from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from utils.test_base import TestBase

class TestLoginPage(TestBase):
    def test_open_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        assert "The Internet" in login_page.get_title()

    def test_login_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("invalid_user", "invalid_password")
    
        error_message = login_page.get_flash_message().text
        assert "Your username is invalid!" in error_message

    def test_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        secure_area_page = SecureAreaPage(self.driver)
        login_page.login("tomsmith","SuperSecretPassword!")

        success_message = secure_area_page.get_flash_message().text
        assert "You logged into a secure area!" in success_message

    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        secure_area_page = SecureAreaPage(self.driver)
        login_page.login("tomsmith","SuperSecretPassword!")
    
        secure_area_page.click_logout_button()
    
        logout_message = login_page.get_flash_message().text
        assert "You logged out of the secure area!" in logout_message
        