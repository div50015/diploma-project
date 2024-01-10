import diploma_project.utils.data
import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def shoult_page_one():
    with step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneOne'))
        results.should(have.text('На любой вкус'))


def go_next_page():
    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()


def shoult_page_two():
    with step('Verify content page 2'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneTwo'))
        results.should(have.text('На любом устройстве'))


# with step('Going next page'):
#     browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

def shoult_page_three():
    with step('Verify content page 3'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneThree'))
        results.should(have.text('Для детей'))


# with step('Going next page'):
#     browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

def shoult_page_four():
    with step('Verify content page 4'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFour'))
        results.should(have.text('Без интернета'))


# with step('Going next page'):
#     browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()


def shoult_page_five():
    with step('Verify content page 5'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFive'))
        results.should(have.text('Своя подписка'))


def go_past_page():
    with step('Going next main page'):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/mainButtonTitle" and @text="Смотреть Wink"]')).click()


def should_main_page():
    with step('Verify content main page'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/logo'))
        results.should(have.text('Wink'))


def go_main_page():
    with step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneOne'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 2'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneTwo'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 3'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneThree'))
        results.should(have.text('Для детей'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 4'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFour'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 5'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFive'))

    with step('Going next main page'):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/mainButtonTitle" and @text="Смотреть Wink"]')).click()
