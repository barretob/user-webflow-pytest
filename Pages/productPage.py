from selenium.webdriver.common.by import By

from Base.base_driver import BaseDriver
from Pages.checkoutPage import chkoutPage


class prodctPage(BaseDriver):
    # LOCATORS
    PRODUCTS_LIST = "//div[@class='card h-100']"
    PRODUCT_CHOICE = "button[class$='btn btn-info']"
    PRODUCT_CHECKOUT = "//a[@class='nav-link btn btn-primary']"
    PRODUCT_NAME = "div/h4/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getProductList(self):
        return self.driver.find_elements(By.XPATH, self.PRODUCTS_LIST)

    def getCheckout(self):
        return self.driver.find_element(By.XPATH, self.PRODUCT_CHECKOUT)

    def getProductNameInList(self, chain):
        return chain.find_element(By.XPATH, self.PRODUCT_NAME)

    def getProductNameChoice(self, chain):
        return chain.find_element(By.CSS_SELECTOR, self.PRODUCT_CHOICE)

    def enterProductName(self, Name):
        products = self.getProductList()
        for product in products:
            productName = self.getProductNameInList(product).text
            if productName == Name:
                self.getProductNameChoice(product).click()  # clicks on item

    def checkout(self):
        self.getCheckout().click()  # clicks checkout
        checkOutPage = chkoutPage(self.driver)
        return checkOutPage
