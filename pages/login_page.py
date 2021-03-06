from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not displayed"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not displayed"

    def register_new_user(self, username, password):
        self.input_value(*LoginPageLocators.REGISTER_EMAIL_INPUT, username)
        self.input_value(*LoginPageLocators.REGISTER_PASSWORD_INPUT, password)
        self.input_value(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_INPUT, password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
