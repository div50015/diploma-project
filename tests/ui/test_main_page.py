from diploma_project.pages.page_open import main_page
import allure


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Страницы')
@allure.story('main')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_main_page_name():
    # GIVEN
    with allure.step('Opening main page'):
        main_page.open_main_page()

    # WHEN
    with allure.step('Opening main page'):
        main_page.open_main_page()

    # THEN
    with allure.step('Should main page'):
        main_page.should_main_page()
