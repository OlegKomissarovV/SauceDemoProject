from .base_page import BasePage
from .locators import ProductsPageLocators


class ProductsPage(BasePage):

    # Проверяет, что текущая страница является страницей корзины
    def should_be_products_page(self):
        # Проверяет, что текущая страница соответствует требованиям
        self.should_be_link("inventory")
        # Проверяет, что текст элемента заглавия страницы
        # соответствует требованиям
        self.should_be_page_title("PRODUCTS", *ProductsPageLocators.TITLE)
        # Проверяет, что товары на страницы соответствуют требованиям
        self.should_be_products_page_inventory_list()
        # Получает элемент корзины на странице
        assert self.browser.find_element(*ProductsPageLocators.SHOP_CART_LINK)

    # Проверяет, что товары на страницы соответствуют требованиям
    def should_be_products_page_inventory_list(self):
        # Получает список элементов товаров на странице
        list_el = self.browser.find_element(*ProductsPageLocators.INVENT_LIST)
        assert (
            len(list_el.get_property("children")) != 0
        ), "there is no products"
