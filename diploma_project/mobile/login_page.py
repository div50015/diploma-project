from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def go_login():
    with step('Going login page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/avatar')).click()


def should_login():
    with step('Verify content login page '):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleTextView'))
        results.should(have.text('Войти или'))
