from diploma_project.pages import page_open
import allure


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Фильтрация')
@allure.story('movies filter')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_movies_page_and_filter():
    # GIVEN
    with allure.step('Opening main page'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # # WHEN
    # with allure.step('Go to Movies page'):
    #     main_page.open_page(main_page, 'Фильмы')
    #
    # with allure.step('Filtering 2023 year'):
    #     main_page.to_do_filtering(main_page)
    #
    # # THEN
    # with allure.step('Should filtering 2023 year '):
    #     main_page.should_movies_and_filter(main_page, 'Все фильмы 2023 года')
