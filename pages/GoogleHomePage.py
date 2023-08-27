from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class GoogleHomePage(BasePage):
    # Locators for the UI elements
    DISMISS_COOKIES_BUTTON = (By.ID, "W0wltc")
    SEARCH_BOX = (By.NAME, "q")

    def dismiss_cookies(self):
        # Click Dismiss Cookies button
        return self.find_element(self.DISMISS_COOKIES_BUTTON).click()

    def type_search_query(self, search_query):
        # Insert the searching query in the search box
        return self.find_element(self.SEARCH_BOX).send_keys(search_query)


    def submit_searching(self):
        return self.find_element(self.SEARCH_BOX).submit()

