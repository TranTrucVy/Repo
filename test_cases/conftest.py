import pytest
from selenium import webdriver


#pytest -s -v .\test_cases\test_login_admin.py --browser chrome

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome",
                    help= "Specify the browesr: chrome or firefox or edge")
    
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()   
    else:
        raise ValueError("Unsupport browser") 
    return driver