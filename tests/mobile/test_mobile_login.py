import diploma_project.utils.data
import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from diploma_project.mobile import start_page,login_page


@allure.epic('MOBILE')
@allure.story('login')
@allure.label('div50015', 'allure8')
@allure.tag('mobile')
def test_login(context):
    # GIVEN
    allure.dynamic.parameter('context', context)
    start_page.go_main_page()

    # WHEN
    login_page.go_login()

    # THEN
    login_page.should_login()
