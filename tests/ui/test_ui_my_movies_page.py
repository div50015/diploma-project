from diploma_project.pages import page_open
import allure


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Страницы')
@allure.story('my_movies')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_my_movies_page():
    # GIVEN
    with allure.step('Opening main page'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Go to My Movies page'):
        main_page.open_page(main_page, 'Моё кино')

    # THEN
    with allure.step('Should My Movies page'):
        main_page.should_page_my_movies(main_page, 'Моё кино')
