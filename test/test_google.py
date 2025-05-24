

class TestGoogleFinance:
    def test_open_google_finance_page(self, app):
        assert "Google Finance" in app.driver.title
        assert app.find_element(app.gf._footer)
        assert app.find_element(app.gf._header)

    def test_compare_current_and_expected_stocks(self, app):
        expected_stock_symbols = ["NFLX", "MSFT", "TSLA", "GOOGL", "AAPL", "AMZN"]
        current_stock_list = app.gf.get_you_may_be_interested_list()

        unexpected_stock = []
        for stock in current_stock_list:
            if stock not in expected_stock_symbols:
                unexpected_stock.append(stock)

        expected_stock = []
        for stock in expected_stock_symbols:
            if stock not in current_stock_list:
                expected_stock.append(stock)

        print(f"Unexpected stocks in the list {unexpected_stock}, Expected stocks that are not in the list {expected_stock}")