import pytest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Specify browser name: chrome, firefox, or IE"
    )


@pytest.fixture(scope="class")
def invokebrowser(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        ser_chrome = Service("E:/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=ser_chrome)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param config: Pytest config object.
    """
    config.addinivalue_line(
        "markers", "hookwrapper: mark the hook as hookwrapper."
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item: Pytest item object.
    """
    pytest_html = item.config.pluginmanager.get_plugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(item.config, file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(config, name):
    driver = config.driver  # Assuming you have driver configured in pytest config
    driver.get_screenshot_as_file(name)
