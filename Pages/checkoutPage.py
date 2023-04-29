from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Pages.purchaeFinalPage import purchFinalPage


class chkoutPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver  # self refers to chkoutpage
    # LOCATORS
    SELECT_CHECKOUT = "button[class$='btn btn-success']"

    def getCheckout(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.SELECT_CHECKOUT)

    def checkout(self):
        self.getCheckout().click()
        purchasePage = purchFinalPage(self.driver)
        return purchasePage

