import tests.ui_tests.page_objects.page as page


class TestUI:
    def test_max_coins_title(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        assert main_page.is_title_matches('Testing')

    def test_max_coins_result_exists(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('1, 5')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result()

    def test_max_coins_result(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('1, 5')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == '10'

    def test_max_coins_single_number(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('1')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == '1'

    def test_max_coins_300_numbers(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input(", ".join(['1' for _ in range(300)]))
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == '300'

    def test_max_coins_number_equals_100(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('100')
        main_page.click_submit_button()
        results_page = page.ResultsPage(browser)

        assert results_page.get_result() == '100'


class TestInvalidUi:
    def test_max_coins_number_is_not_number(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('asd')
        main_page.click_submit_button()
        error_page = page.ErrorPage(browser)

        assert error_page.is_title_matches("400 Bad Request")

    def test_max_coins_numbers_without_comma(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('1 2 3')
        main_page.click_submit_button()
        error_page = page.ErrorPage(browser)

        assert error_page.is_title_matches("400 Bad Request")

    def test_max_coins_number_too_large(self, browser):
        browser.get("http://127.0.0.1:5000")
        main_page = page.MainPage(browser)
        main_page.fill_input('101')
        main_page.click_submit_button()
        error_page = page.ErrorPage(browser)

        assert error_page.is_title_matches("400 Bad Request")
