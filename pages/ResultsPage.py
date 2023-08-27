from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ResultsPage(BasePage):

    SEARCH_RESULTS = (By.XPATH, "//*[@id='rso']//cite")

    def assertFlukeInFirstResult(self):
        results = self.find_elements(self.SEARCH_RESULTS)
        first_result = results[0].text
        assert "www.fluke.com/" in first_result



