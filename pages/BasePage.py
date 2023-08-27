from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT = 20  # Maximum waiting time

    def __init__(self, driver):
        self.driver = driver

    # Wait for element to be visible
    def wait_for_element(self, locator, time=TIMEOUT):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    # Wait for element to be visible then return it
    def find_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    # Wait for elements to be visible then return them
    def find_elements(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_elements(*locator)