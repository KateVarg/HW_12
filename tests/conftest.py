import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_setting():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1800
    browser.config.window_width = 1200


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Браузер, в котором запущены тесты',
        choices=['chrome', 'firefox'],
        default='chrome'
    )


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    browser_name = request.config.getoption('--browser')
    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
        options=options)

    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()

