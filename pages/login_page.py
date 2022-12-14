from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_link("https://www.saucedemo.com/")
        # Проверяет, что элемент для ввода имени пользователя
        # имеется на текущей странице
        assert self.element_is_present(*LoginPageLocators.INPUT_USERNAME)
        # Проверяет, что элемент для ввода пароля имеется на текущей странице
        assert self.element_is_present(*LoginPageLocators.INPUT_PASSWORD)
        # Проверяет, что элемент кнопки для подтверждения
        # имеется на текущей странице
        assert self.element_is_present(*LoginPageLocators.LOGIN_BTN)
        # Проверяет, что имена пользователей имеются на текущей странице
        assert self.element_is_present(*LoginPageLocators.LOGIN_CREDENTIALS)
        # Проверяет, что пароль пользователй имеется на текущей странице
        assert self.element_is_present(*LoginPageLocators.LOGIN_PASSWORD)

    def register_user(self, username, password):
        # n = 1
        # h = self.get_text(n, *LoginPageLocators.LOGIN_CREDENTIALS)
        # w = self.get_text(n, *LoginPageLocators.LOGIN_PASSWORD)
        # Имя пользователя передается текстовому элементу
        # на странице авторизации
        self.browser.find_element(*LoginPageLocators.INPUT_USERNAME).send_keys(
            username
        )
        # Пароль передается текстовому элементу на странице авторизации
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(
            password
        )
        # Нажимается кнопка "LOGIN"
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()
