import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest:

    """ Test fixture used to setting up the
        driver and run the environment.
        It closes the driver after test is done."""
    @pytest.fixture
    def driver(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")  # Optional: run driver in a headless mode

        # Setting up the driver path as ChromeDriverManager
        chromedriver_path = ChromeDriverManager().install()

        service = Service(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://www.google.com")
        yield self.driver
        self.driver.quit()