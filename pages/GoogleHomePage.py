from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class GoogleHomePage(BasePage):

    DISMISS_COOKIES_BUTTON = (By.ID, "W0wltc")
    SEARCH_BOX = (By.NAME, "q")

    def dismissCookies(self):
        return self.find_element(self.DISMISS_COOKIES_BUTTON).click()

    def typeSearchQuery(self, search_query):
        return self.find_element(self.SEARCH_BOX).send_keys(search_query)


    def submitSearching(self):
        return self.find_element(self.SEARCH_BOX).submit()

