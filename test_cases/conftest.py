import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test Run --> Browser Chrome")
        driver = webdriver.Chrome()
    elif browser == "edge":
        print("Test Run --> Browser Edge")
        driver = webdriver.Firefox()
    elif browser == "firefox":
        print("Test Run --> Browser Firefox")
        driver = webdriver.Firefox()
    else:
        print("Test Run --> Browser Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def setup_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com")
    driver.implicitly_wait(10)
    return driver
