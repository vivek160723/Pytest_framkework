import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    print("Launching browser")
    yield
    print("Closing browser")

@pytest.fixture()
def setupp(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    elif browser=="edge":
        driver = webdriver.Edge()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")