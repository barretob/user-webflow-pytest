
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="class")
def setup(request):
    # initiation of website w/ chrome webdriver
    s = Service('/Users/bryanbarreto/Downloads/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(service=s)
    # driver.implicitly_wait(4)
    # wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    # teardown
    driver.close()
