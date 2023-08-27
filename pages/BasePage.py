from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

        # Waiting for element located at passed selector
    def wait_for_element(self, locator, time = TIMEOUT):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

        """ Wrapped selenium based find_element method includes waiting method.
                    Waiting until element is visible, then return the element."""
    def find_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)


    def find_elements(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_elements(*locator)