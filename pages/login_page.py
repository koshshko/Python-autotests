from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, '//h3[@data-test="error"]')
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def enter_username(self, username):
        self.find_element(*self.USERNAME_FIELD).send_keys(username)
        
    def enter_password(self, password):
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)
        
    def click_login_button(self):
        self.find_element(*self.LOGIN_BUTTON).click()
        
    def is_error_message_displayed(self):
        return self.is_element_visible(*self.ERROR_MESSAGE)
        
    def get_current_url(self):
        return self.driver.current_url
