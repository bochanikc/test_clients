import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", "-B",
        action="store",
        default="chrome",
        help="choose your browser"
    )

    parser.addoption(
        "--url", "-U",
        action="store",
        default="http://clients.homestead/",
        help="Write url"
    )


# @pytest.fixture
# def browser(request):
#     browser_param = request.config.getoption("--browser")
#     if browser_param == "chrome":
#         driver = webdriver.Chrome()
#     elif browser_param == "firefox":
#         driver = webdriver.Firefox()
#     elif browser_param == "ie":
#         driver = webdriver.Ie()
#     else:
#         raise Exception(f"{browser_param} is not supported.")
#
#     driver.implicitly_wait(20)
#     request.addfinalizer(driver.close)
#     driver.get(request.config.getoption("--url"))
#
#     return driver


@pytest.fixture(params=["chrome"])
def browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    elif browser_param == "ie":
        driver = webdriver.Ie()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(5)
    driver.set_window_size(1920, 1080)
    driver.get(request.config.getoption("--url"))
    request.addfinalizer(driver.quit)

    return driver
