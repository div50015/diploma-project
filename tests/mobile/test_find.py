import diploma_project.utils.data
import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from diploma_project.mobile import start_page,find_page


def test_find(context):
    # GIVEH
    allure.dynamic.parameter('context', context)
    start_page.go_main_page()

    # WHEN
    find_page.go_find()

    # THEN
    find_page.should_find()
