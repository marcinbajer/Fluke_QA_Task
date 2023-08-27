import pytest

from pages.GoogleHomePage import GoogleHomePage
from pages.ResultsPage import ResultsPage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):

    """
    A test method which performs the following steps:
    1. Opens the www.google.com website.
    2. Enters the 'fluke' phrase into the search box.
    3. Submits the search query.
    4. Checks if www.fluke.com appears as the first result.
    """
    def test_google_search_fluke(self, driver, query="fluke"):
        # Creating the object of the Google Home page
        home_page = GoogleHomePage(self.driver) # Creating the object of the Google home page
        home_page.type_search_query(query)
        home_page.submit_searching()

        # Creating the object of the Google Results page
        results = ResultsPage(self.driver) # Creating the object of the Google results page
        results.assert_fluke_in_first_result()

# Run the tests when the script is executed
if __name__ == "__main__":
    pytest.main()
