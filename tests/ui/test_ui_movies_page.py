from diploma_project.pages import page_open
import allure


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Страницы')
@allure.story('movies')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_movies_page():
    # GIVEN
    with allure.step('Opening main page'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Go to Movies page'):
        main_page.open_page(main_page, 'Фильмы')

    # THEN
    with allure.step('Should Movies page'):
        main_page.should_page_my_movies(main_page, 'Фильмы по жанрам')
