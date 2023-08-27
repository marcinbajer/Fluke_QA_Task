import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest:

    """
    Test fixture used to set up the driver and run the environment.
    It closes the driver after the test is done.
    """
    @pytest.fixture
    def driver(self):
        # Optional: Run the driver in headless mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Optional: run driver in a headless mode

        # Setting up the driver path as ChromeDriverManager
        chromedriver_path = ChromeDriverManager().install()

        # Create a service for Chrome driver
        service = Service(executable_path=chromedriver_path)

        # Create an instance of Chrome webdriver with the defined options and service
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the Google homepage
        self.driver.get("https://www.google.com")

        # Yield the driver for the test
        yield self.driver

        # Quit the driver after the test is done
        self.driver.quit()