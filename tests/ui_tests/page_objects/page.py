from tests.ui_tests.page_objects.locators import MainPageLocators, ResultsPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self, title):
        return title == self.driver.title


class MainPage(BasePage):

    def fill_input(self, text):
        elem = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        elem.send_keys(text)

    def click_submit_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class ResultsPage(BasePage):
    def get_result(self):
        element = self.driver.find_element(*ResultsPageLocators.RESULT)
        return element.text


class ErrorPage(BasePage):
    pass
