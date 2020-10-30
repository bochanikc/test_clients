import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", "-B",
        action="store",
        default=None,
        help="choose your browser"
    )

    parser.addoption(
        "--url", "-U",
        action="store",
        default="http://clients.homestead:1370/",
        help="Write url"
    )


@pytest.fixture(params=["chrome"])
def browser(request):
    if request.config.getoption("--browser") is None:
        browser_param = request.param
    else:
        browser_param = request.config.getoption("--browser")

    driver = selection_browser(browser_param)

    driver.implicitly_wait(5)
    driver.set_window_size(1920, 1080)
    driver.get(request.config.getoption("--url"))
    request.addfinalizer(driver.quit)
    return driver


def selection_browser(browser_param):
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    elif browser_param == "ie":
        driver = webdriver.Ie()
    elif browser_param == "Remote":
        driver = webdriver.Remote("http://172.16.169.137:4444/",
                                  desired_capabilities={'browserName': 'chrome'})
    else:
        raise Exception(f"{browser_param} is not supported!")
    return driver
