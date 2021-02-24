import unittest
from selenium import webdriver
import time
import page


class TestVigo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:\\Program Files (x86)\\chromedriver.exe")
        self.driver.get("https://qa.staging.vigoshop.si/")

    def test_1_order(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_article1()

        articlePage = page.ArticlePage(self.driver)
        articlePage.click_cart_button()

        shoppingCartPage = page.ShoppingCartPage(self.driver)
        shoppingCartPage.click_checkout_button()

        checkoutPage = page.CheckoutPage(self.driver)
        checkoutPage.phone_element = '040123321'
        checkoutPage.first_name_Element = 'Janez'
        checkoutPage.last_name_Element = 'Vajkard Valvasor'
        time.sleep(2)
        checkoutPage.click_placeorder_button()
        time.sleep(2)
        assert checkoutPage.is_error_found()
        checkoutPage.email_element = 'janezv@gmail.com'
        checkoutPage.address_element = 'Slavčeva 5'
        checkoutPage.post_code_element = '4000'
        time.sleep(3)
        checkoutPage.click_placeorder_button()

        orderCompletePage = page.OrderCompletePage(self.driver)
        assert orderCompletePage.is_order_complete()
        time.sleep(3)

    def test_2_empty_shopping_cart(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_article3()

        articlePage = page.ArticlePage(self.driver)
        articlePage.click_qty3()
        time.sleep(2)
        articlePage.click_cart_button()
        time.sleep(2)

        shoppingCartPage = page.ShoppingCartPage(self.driver)
        shoppingCartPage.click_remove_articles()
        assert shoppingCartPage.is_shopping_cart_empty()
        time.sleep(2)
        shoppingCartPage.click_back_to_shop()

        assert mainPage.is_zero_in_cart()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
