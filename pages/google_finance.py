import json
import os


class GoogleFinancePage:
    def __init__(self, app):
        self.app = app


    _you_may_be_interested_table = "//section[@aria-labelledby='smart-watchlist-title']"
    _footer = "//div[@role='contentinfo']"
    _header = "//header[@role='banner']"

    def get_you_may_be_interested_list(self):
        stock_list = self.app.find_elements(locator=f"{self._you_may_be_interested_table}//ul/li//div[@class='COaKTb']")
        return [stock.text for stock in stock_list]
