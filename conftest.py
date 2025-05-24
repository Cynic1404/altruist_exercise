from base.seleniumwebdriver import Application
import pytest

fixture = None

def pytest_addoption(parser):
    parser.addoption('--wait', action="store", default=5)
    parser.addoption('--browser', action="store", default="chrome")


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--wait")

    if fixture is None:
        fixture = Application(browser=browser, wait=wait)
        try:
            fixture.driver.get("https://www.google.com/finance/")
        except Exception:
            fixture.close()
            fixture = None
            raise #to keep original error
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    yield
    if fixture:
        fixture.close()

