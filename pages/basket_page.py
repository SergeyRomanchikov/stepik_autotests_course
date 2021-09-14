from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_item_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM)

    def is_basket_is_empty_message_displayed(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)