import os
import pytest

from selene import browser
from appium import webdriver
from qa_guru_python_22.utils import allure_attach
from dotenv import load_dotenv
from allure_commons._allure import step


def pytest_addoption(parser):
    parser.addoption("--context",
                     default="bstack",
                     help="Specify the test context")


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f"Warning: Configuration file '{env_file_path}' not found.")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from config import config_app
    options = config_app.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(
        options.get_capability('remote_url'), options=options)

    browser.config.timeout = 10.0

    yield

    allure_attach.screenshot()

    allure_attach.page_source_xml()

    session_id = browser.driver.session_id

    with step('tear down app session'):
        browser.quit()

    if context == 'bstack':
        with step('tear down app session'):
            browser.quit()
        allure_attach.bstack_video(session_id)
