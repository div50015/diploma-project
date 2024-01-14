from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def go_find():
    with step('Going find page'):
        browser.element(
            (AppiumBy.XPATH,
             '//android.widget.LinearLayout[@resource-id='
             '"ru.rt.video.app.mobile:id/actionsContainer"]'
             '/android.widget.ImageView[1]'
             )
        ).click()


def should_find():
    with step('Verify content find page '):
        results = browser.element(
            (AppiumBy.ID, 'ru.rt.video.app.mobile:id/tvTitle')
        )
        results.should(have.text('Поиск'))
