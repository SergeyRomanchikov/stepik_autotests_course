from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE_FORM), "Product page not displayed"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name_from_alert(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CONFIRM_ALERT).text

    def get_basket_price_from_basket_alert(self):
        basket_price_from_basket_alert = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_BASKET_ALERT).text
        print(f"Basket price from basket alert: {basket_price_from_basket_alert}")
        return basket_price_from_basket_alert

    def should_be_confirm_alert(self):
        assert self.is_element_present(*ProductPageLocators.CONFIRM_ALERT)

    def should_be_basket_price_alert(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_IN_BASKET_ALERT)

    def is_basket_price_equals_product_price(self):
        assert self.get_basket_price_from_basket_alert() == self.get_product_price(), "Price not equals"

    def is_product_name_in_alert_equals_product_name(self):
        assert self.get_product_name() == self.get_product_name_from_alert()

    def is_success_message_after_adding_product_to_basket_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRM_ALERT)

    def is_success_message_after_adding_product_to_basket_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRM_ALERT)