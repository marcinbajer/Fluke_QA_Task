import pytest

from pages.GoogleHomePage import GoogleHomePage
from pages.ResultsPage import ResultsPage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):

    """A test method which performing following steps:
    1. Opens the www.google.com website.
    2. Pass the 'fluke' phrase to the search box.
    3. Submit the search query
    4. Check if www.fluke.com appear as a first result"""
    def test_google_search_fluke(self, driver, query="fluke"):
        assert "Google" in self.driver.title
        home_page = GoogleHomePage(self.driver) # Creating the object of the Google home page
        home_page.typeSearchQuery(query)
        home_page.submitSearching()

        results = ResultsPage(self.driver) # Creating the object of the Google results page
        results.assertFlukeInFirstResult()


if __name__ == "__main__":
    pytest.main()
