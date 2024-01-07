import diploma_project.utils.data
import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_wiki_start(context):
    allure.dynamic.parameter('context', context)
    check_txt = diploma_project.utils.data.set_check_text(context)

    with step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneOne'))
        results.should(have.text('На любой вкус'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 2'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneTwo'))
        results.should(have.text('На любом устройстве'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 3'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneThree'))
        results.should(have.text('Для детей'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 4'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFour'))
        results.should(have.text('Без интернета'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 5'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFive'))
        results.should(have.text('Своя подписка'))

    with step('Going next main page'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/mainButtonTitle" and @text="Смотреть Wink"]')).click()

    with step('Verify content main page'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/logo'))
        results.should(have.text('Wink'))


def test_wiki_login(context):
    allure.dynamic.parameter('context', context)
    check_txt = diploma_project.utils.data.set_check_text(context)

    with step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneOne'))
        results.should(have.text('На любой вкус'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 2'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneTwo'))
        results.should(have.text('На любом устройстве'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 3'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneThree'))
        results.should(have.text('Для детей'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 4'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFour'))
        results.should(have.text('Без интернета'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 5'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFive'))
        results.should(have.text('Своя подписка'))

    with step('Going next main page'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/mainButtonTitle" and @text="Смотреть Wink"]')).click()

    with step('Verify content main page'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/logo'))
        results.should(have.text('Wink'))

    with step('Going login page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/avatar')).click()

    with step('Verify content login page '):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleTextView'))
        results.should(have.text('Войти или'))


def test_wiki_find(context):
    allure.dynamic.parameter('context', context)
    check_txt = diploma_project.utils.data.set_check_text(context)

    with step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneOne'))
        results.should(have.text('На любой вкус'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 2'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneTwo'))
        results.should(have.text('На любом устройстве'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 3'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneThree'))
        results.should(have.text('Для детей'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 4'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFour'))
        results.should(have.text('Без интернета'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 5'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFive'))
        results.should(have.text('Своя подписка'))

    with step('Going next main page'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/mainButtonTitle" and @text="Смотреть Wink"]')).click()

    with step('Verify content main page'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/logo'))
        results.should(have.text('Wink'))

    with step('Going find page'):
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="ru.rt.video.app.mobile:id/actionsContainer"]/android.widget.ImageView[1]')).click()

    with step('Verify content find page '):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/tvTitle'))
        results.should(have.text('Поиск'))


def test_wiki_movies(context):
    allure.dynamic.parameter('context', context)
    check_txt = diploma_project.utils.data.set_check_text(context)

    with step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneOne'))
        results.should(have.text('На любой вкус'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 2'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneTwo'))
        results.should(have.text('На любом устройстве'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 3'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneThree'))
        results.should(have.text('Для детей'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 4'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFour'))
        results.should(have.text('Без интернета'))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()

    with step('Verify content page 5'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFive'))
        results.should(have.text('Своя подписка'))

    with step('Going next main page'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/mainButtonTitle" and @text="Смотреть Wink"]')).click()

    with step('Verify content main page'):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/logo'))
        results.should(have.text('Wink'))

    with step('Going movies page'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/navigation_bar_item_small_label_view" and @text="Фильмы"]')).click()

    with step('Verify content movies page '):
        results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/title'))
        results.should(have.text('Фильмы'))





