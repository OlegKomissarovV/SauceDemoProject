import pytest
from .pages.products_page import ProductsPage
from .pages.login_page import LoginPage


link = "https://www.saucedemo.com/"


# TC_003.00.01, TC_003.00.02, TC_003.00.03, TC_003.00.04
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
# Тест проверяет, что пользователь может перейти со страницы авторизации
# на страницу каталога товаров
def test_user_can_go_to_products_page(browser, username, password):
    # Создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # Открывает страницу авторизации
    page.open_page()
    # Проверяет, что текущая страница является страницей авторизации
    page.should_be_login_page()
    # Авторизация пользователя
    page.register_user(username, password)
    # Создает экземпляр главной страницы - Main Page
    page = ProductsPage(browser, link)
    # Проверяет, что текущая страница является страницей каталогом товаров
    page.should_be_products_page()


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
# Свой тест
def test_register_user(browser, username, password):
    # Создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # Открывает страницу авторизации
    page.open_page()
    # Авторизация пользователя
    page.register_user(username, password)
