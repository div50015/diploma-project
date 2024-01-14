from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def should_page_one():
    with step('Verify content page 1'):
        results = browser.element(
            (AppiumBy.ID,
             'ru.rt.video.app.mobile:id/titleSceneOne')
        )
        results.should(have.text('На любой вкус'))
    go_next_page()


def go_next_page():
    with step('Going next page'):
        browser.element(
            (AppiumBy.ID,
             'ru.rt.video.app.mobile:id/mainButtonTitle'
             )
        ).click()


def should_page_two():
    with step('Verify content page 2'):
        results = browser.element(
            (AppiumBy.ID,
             'ru.rt.video.app.mobile:id/titleSceneTwo'
             )
        )
        results.should(have.text('На любом устройстве'))
    go_next_page()


def should_page_three():
    with step('Verify content page 3'):
        results = browser.element(
            (AppiumBy.ID,
             'ru.rt.video.app.mobile:id/titleSceneThree'
             )
        )
        results.should(have.text('Для детей'))
    go_next_page()


def should_page_four():
    with step('Verify content page 4'):
        results = browser.element(
            (AppiumBy.ID,
             'ru.rt.video.app.mobile:id/titleSceneFour'
             )
        )
        results.should(have.text('Без интернета'))
    go_next_page()


def should_page_five():
    with step('Verify content page 5'):
        results = browser.element(
            (AppiumBy.ID,
             'ru.rt.video.app.mobile:id/titleSceneFive'
             )
        )
        results.should(have.text('Своя подписка'))
    go_past_page()


def go_past_page():
    with step('Going next main page'):
        browser.element(
            (AppiumBy.XPATH,
             '//android.widget.TextView'
             '[@resource-id="ru.rt.video.app.mobile:id/'
             'mainButtonTitle" and @text="Смотреть Wink"]'
             )
        ).click()


def should_main_page():
    with step('Verify content main page'):
        results = browser.element(
            (AppiumBy.ID, 'ru.rt.video.app.mobile:id/logo')
        )
        results.should(have.text('Wink'))


def go_main_page():
    with step('Going next page'):
        browser.element(
            (AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')
        ).click()

    with step('Going next page'):
        browser.element(
            (AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')
        ).click()

    with step('Going next page'):
        browser.element(
            (AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')
        ).click()

    with step('Going next page'):
        browser.element(
            (AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')
        ).click()

    with step('Going next main page'):
        browser.element(
            (AppiumBy.XPATH,
             '//android.widget.TextView'
             '[@resource-id="ru.rt.video.app.mobile:id/'
             'mainButtonTitle" and @text="Смотреть Wink"]'
             )
        ).click()
