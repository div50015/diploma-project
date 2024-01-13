import pytest
from selene import browser
from selenium import webdriver
from diploma_project.utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://wink.ru'
    browser.config.timeout = 4.0
    browser.config.window_width = 1900
    browser.config.window_height = 1080

    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    browser.config.driver_options = driver_options

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
