from diploma_project.pages.page_open import main_page
import allure


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Страницы')
@allure.story('serials')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_movies_page_name():
    # GIVEN
    with allure.step('Opening main page'):
        main_page.open_main_page()

    # WHEN
    with allure.step('Go to Serials page'):
        main_page.open_page('Сериалы')

    # THEN
    with allure.step('Should Serials page'):
        main_page.should_page_serials('Сериалы')
