import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def scrollDown(self):
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(3)

    # create a method for waits being used
    def wait_until_presence_of_all_elements_located(self, selector_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_elements = wait.until(EC.presence_of_all_elements_located((selector_type, locator)))
        return list_elements
