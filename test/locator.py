from selenium.webdriver.common.by import By


class MainPageLocators(object):
    ARTICLE_1 = (
        By.XPATH, '//a[@href="https://qa.staging.vigoshop.si/izdelek/virgo-brezzicni-slusalki-za-telefon/"]')

    ARTICLE_3 = (
        By.XPATH, '//a[@href="https://qa.staging.vigoshop.si/izdelek/six-pack-komplet-za-fit-postavo/"]')

    NUMBER_OF_ARTICLES_IN_CART = (
        By.CLASS_NAME, 'cart-customlocation')


class ArticlePageLocators(object):
    CART_BUTTON = (
        By.CLASS_NAME, 'single_add_to_cart_button')

    QTY_3_TD = (
        By.CLASS_NAME, 'mp_product_qty_3')


class ShoppingCartPageLocators(object):
    CHECKOUT_BUTTON = (By.CLASS_NAME, 'checkout-button')

    REMOVE_ARTICLES = (By.CLASS_NAME, 'mp_remove')

    EMPTY_CART = (By.CLASS_NAME, 'cart-empty')

    BACK_TO_SHOP = (By.CLASS_NAME, 'wc-backward')


class CheckoutPageLocators(object):
    PLACEORDER_BUTTON = (By.ID, 'place_order')


class OrderCompletePageLocators(object):
    ORDER_OK_SPAN = (By.CLASS_NAME, 'order-ok')
