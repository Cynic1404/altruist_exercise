

class TestGoogleFinance:
    def test_open_google_finance_page(self, app):
        assert "Google Finance" in app.driver.title
        assert app.find_element(app.gf._footer)
        assert app.find_element(app.gf._header)

    def test_compare_current_and_expected_stocks(self, app):
        expected_stock_symbols = set(["NFLX", "MSFT", "TSLA", "GOOG", "AAPL", "AMZN"])
        current_stock_list = set(app.gf.get_you_may_be_interested_list())

        unexpected_stock = current_stock_list - expected_stock_symbols
        missing_expected_stock = expected_stock_symbols - current_stock_list

        print(f"Unexpected stocks in the list {unexpected_stock}, Expected stocks that are not in the list {missing_expected_stock}")