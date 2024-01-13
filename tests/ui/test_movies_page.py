from diploma_project.pages.page_open import main_page
import allure


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Страницы')
@allure.story('movies')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_movies_page_name():
    # GIVEN
    with allure.step('Opening main page'):
        main_page.open_main_page()

    # WHEN
    with allure.step('Go to Movies page'):
        main_page.open_page('Фильмы')

    # THEN
    with allure.step('Should Movies page'):
        main_page.should_page_my_movies('Фильмы по жанрам')


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Фильтрация')
@allure.story('movies filter')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_movies_page_filter():
    # GIVEN
    with allure.step('Opening main page'):
        main_page.open_main_page()

    # WHEN
    with allure.step('Go to Movies page'):
        main_page.open_page('Фильмы')

    with allure.step('Filtering 2023 year'):
        main_page.to_do_filtering()

    # THEN
    with allure.step('Should filtering 2023 year '):
        main_page.should_movies_and_filter('Все фильмы 2023 года')


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Фильтрация')
@allure.story('movies filter and sort')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_movies_page_sort():
    # GIVEN
    with allure.step('Opening main page'):
        main_page.open_main_page()

    # WHEN
    with allure.step('Go to Movies page'):
        main_page.open_page('Фильмы')

    with allure.step('Filtering 2023 year and sort rating'):
        main_page.to_do_filtring_and_sorting()

    # THEN
    with allure.step('Should sort rating'):
        main_page.should_page_movies_and_filter_and_sort()
