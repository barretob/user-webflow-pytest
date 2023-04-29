
from selenium.webdriver.common.by import By

from Base.base_driver import BaseDriver


class purchFinalPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # LOCATORS
    COUNTRY_NAME = "country"
    COUNTRY_LIST = "//div[@class='suggestions']//a"
    COUNTRY_CHOICE = "//a[normalize-space()='India']"
    SELECT_CHECKBOX = "//div[@class='checkbox checkbox-primary']"
    SELECT_SUBMIT = "[type='submit']"
    VALIDATE_MESSAGE = "alert-success"

    def getCountryName(self):
        return self.driver.find_element(By.ID, self.COUNTRY_NAME)

    def getCountryList(self):
        return self.wait_until_presence_of_all_elements_located(By.XPATH, self.COUNTRY_LIST)

    def getCountryChoice(self, chain):
        return chain.find_element(By.XPATH, self.COUNTRY_CHOICE)

    def getCheckBoxBtn(self):
        return self.driver.find_element(By.XPATH, self.SELECT_CHECKBOX)

    def getSubmitBtn(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.SELECT_SUBMIT)

    def getMsg(self):
        return self.driver.find_element(By.CLASS_NAME, self.VALIDATE_MESSAGE)

    def selectCountry(self, country):
        self.getCountryName().send_keys(country)
        elementList = self.getCountryList()
        countryList = elementList
        for countri in countryList:
            if "India" in countri.text:
                self.getCountryChoice(countri).click()
                break

    def selectCheckbox(self):
        self.getCheckBoxBtn().click()

    def selectsSubmit(self):
        self.getSubmitBtn().click()

    def validatePurchaseMsg(self):
        successText = self.getMsg().text
        assert "Success! Thank you!" in successText
