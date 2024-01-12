from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def go_movies():
    with step('Going movies page'):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/navigation_bar_item_small_label_view" and @text="Фильмы"]')).click()


def should_movies():
    with step('Verify content movies page '):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/title'))
        results.should(have.text('Фильмы'))
