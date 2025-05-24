from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.google_finance import GoogleFinancePage


class Application:
    def __init__(self, browser, wait):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wait = wait
        self.gf = GoogleFinancePage(self)

    def find_element(self, locator, time_to_wait=None, locatorType='xpath'):
        time_to_wait = self.set_default_time(time_to_wait)
        try:
            driver = self.driver
            wait = WebDriverWait(driver, time_to_wait)
            element = wait.until(ec.visibility_of_element_located((getattr(By, locatorType.upper()), locator)))
            return element
        except:
            raise NoSuchElementException('Element not found: locator type = %s, locator = %s' % (locatorType, locator))

    def find_elements(self, locator, locatorType='xpath'):
        try:
            driver = self.driver
            elements = driver.find_elements(getattr(By, locatorType.upper()), locator)
            return elements
        except:
            raise NoSuchElementException('Element not found: locator type = %s, locator = %s' % (locatorType, locator))



    def set_default_time(self, time):
        if time == None:
            time = self.wait
        return int(time)

    def close(self):
        self.driver.quit()
