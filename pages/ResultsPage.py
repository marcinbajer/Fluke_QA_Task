from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ResultsPage(BasePage):
    # Locators for the UI elements
    SEARCH_RESULTS = (By.XPATH, "//*[@id='rso']//cite")

    def assert_fluke_in_first_result(self):
        # Find all the search results on the Results Page
        results = self.find_elements(self.SEARCH_RESULTS)

        # Get text of the first result
        first_result = results[0].text

        # Check if the 'www.fluke.com' appear in the very first search result
        assert "www.fluke.com" in first_result
        # checking if test passing while PR



