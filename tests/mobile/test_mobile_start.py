import diploma_project.utils.data
import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from diploma_project.mobile import start_page

@allure.epic('MOBILE')
@allure.story('main page')
@allure.label('div50015', 'allure8')
@allure.tag('mobile')
def test_start(context):
    # GIVEN
    allure.dynamic.parameter('context', context)

    # THEN
    start_page.shoult_page_one()
    start_page.go_next_page()
    start_page.shoult_page_two()
    start_page.go_next_page()
    start_page.shoult_page_three()
    start_page.go_next_page()
    start_page.shoult_page_four()
    start_page.go_next_page()
    start_page.shoult_page_five()
    start_page.go_past_page()
    start_page.should_main_page()



    # with step('Verify content page 1'):
    #     results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneOne'))
    #     results.should(have.text('На любой вкус'))
    #
    # with step('Going next page'):
    #     browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()
    #
    # with step('Verify content page 2'):
    #     results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneTwo'))
    #     results.should(have.text('На любом устройстве'))
    #
    # with step('Going next page'):
    #     browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()
    #
    # with step('Verify content page 3'):
    #     results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneThree'))
    #     results.should(have.text('Для детей'))
    #
    # with step('Going next page'):
    #     browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()
    #
    # with step('Verify content page 4'):
    #     results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFour'))
    #     results.should(have.text('Без интернета'))
    #
    # with step('Going next page'):
    #     browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/mainButtonTitle')).click()
    #
    # with step('Verify content page 5'):
    #     results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/titleSceneFive'))
    #     results.should(have.text('Своя подписка'))
    #
    # with step('Going next main page'):
    #     browser.element((AppiumBy.XPATH,
    #                      '//android.widget.TextView[@resource-id="ru.rt.video.app.mobile:id/mainButtonTitle" and @text="Смотреть Wink"]')).click()
    #
    # with step('Verify content main page'):
    #     results = browser.element((AppiumBy.ID, 'ru.rt.video.app.mobile:id/logo'))
    #     results.should(have.text('Wink'))
