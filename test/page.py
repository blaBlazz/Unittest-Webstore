from locator import *
from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait


class EmailElement(BasePageElement):
    locator = 'billing_email'


class PhoneElement(BasePageElement):
    locator = 'billing_phone'


class FirstNameElement(BasePageElement):
    locator = 'billing_first_name'


class LastNameElement(BasePageElement):
    locator = 'billing_last_name'


class AddressElement(BasePageElement):
    locator = 'billing_address_1'


class PostCodeElement(BasePageElement):
    locator = 'billing_postcode'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        return "Vigoshop" in self.driver.title

    def click_article1(self):
        element = self.driver.find_element(*MainPageLocators.ARTICLE_1)
        element.click()

    def click_article3(self):
        element = self.driver.find_element(*MainPageLocators.ARTICLE_3)
        element.click()

    def is_zero_in_cart(self):
        number_in_cart = MainPageLocators.NUMBER_OF_ARTICLES_IN_CART
        driver = self.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*number_in_cart))
        element = self.driver.find_element(*number_in_cart)
        return "0" in element.get_attribute('innerHTML')


class ArticlePage(BasePage):

    def click_cart_button(self):
        element = self.driver.find_element(*ArticlePageLocators.CART_BUTTON)
        element.click()

    def click_qty3(self):
        element = self.driver.find_element(*ArticlePageLocators.QTY_3_TD)
        element.click()


class ShoppingCartPage(BasePage):

    def click_checkout_button(self):
        element = self.driver.find_element(
            *ShoppingCartPageLocators.CHECKOUT_BUTTON)
        element.click()

    def click_remove_articles(self):
        element = self.driver.find_element(
            *ShoppingCartPageLocators.REMOVE_ARTICLES)
        element.click()

    def is_shopping_cart_empty(self):
        empty_cart = ShoppingCartPageLocators.EMPTY_CART
        driver = self.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*empty_cart))
        element = self.driver.find_element(*empty_cart)
        return "Vaša košarica je trenutno prazna" in element.get_attribute('innerHTML')

    def click_back_to_shop(self):
        element = self.driver.find_element(
            *ShoppingCartPageLocators.BACK_TO_SHOP)
        element.click()


class CheckoutPage(BasePage):

    email_element = EmailElement()
    phone_element = PhoneElement()
    first_name_Element = FirstNameElement()
    last_name_Element = LastNameElement()
    address_element = AddressElement()
    post_code_element = PostCodeElement()

    def click_placeorder_button(self):
        element = self.driver.find_element(
            *CheckoutPageLocators.PLACEORDER_BUTTON)
        element.click()

    def is_error_found(self):
        return "Podatek je obvezen" in self.driver.page_source


class OrderCompletePage(BasePage):

    def is_order_complete(self):
        order_ok = OrderCompletePageLocators.ORDER_OK_SPAN
        driver = self.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*order_ok))
        element = self.driver.find_element(*order_ok)
        return "uspešno oddano" in element.get_attribute('innerHTML')
