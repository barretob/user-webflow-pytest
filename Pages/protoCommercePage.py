from selenium.webdriver.common.by import By

from Base.base_driver import BaseDriver
from Pages.productPage import prodctPage


class protoComPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    NAVIGATE_TO_SHOP = "a[href*='shop']"

    def getNavigateToShopBtn(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.NAVIGATE_TO_SHOP)

    def navigateToShop(self):
        self.getNavigateToShopBtn().click()
        productPage = prodctPage(self.driver)
        return productPage
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()


# Refactor each Page instance
# locators
# methods to return full locator code
# full methods
