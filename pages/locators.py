from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_PAGE_FORM = (By.CSS_SELECTOR, "#product_page")
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'add-to-basket')]")
    CONFIRM_ALERT = (By.XPATH, "//div[@class = 'alert alert-safe alert-noicon alert-success  fade in'][1]")
    PRODUCT_NAME_IN_CONFIRM_ALERT = (
        By.XPATH, "//div[@class = 'alert alert-safe alert-noicon alert-success  fade in'][1]//strong")
    BASKET_PRICE_IN_BASKET_ALERT = (By.XPATH, "//a[@class = 'btn btn-info']/ancestor::div/p/strong")

    PRODUCT_PRICE = (By.XPATH, "//p[@class = 'price_color']")
    PRODUCT_NAME = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
