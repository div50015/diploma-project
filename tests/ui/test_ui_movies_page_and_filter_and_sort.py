from diploma_project.pages import page_open
import allure


@allure.epic('UI')
@allure.feature('Фильтрация')
@allure.story('movies filter and sort')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_movies_page_and_filter():
    # GIVEN
    with allure.step('Opening main page'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Go to Movies page'):
        main_page.open_page(main_page, 'Фильмы')

    with allure.step('Filtering 2023 year and sort rating'):
        main_page.to_do_filtring_and_sorting(main_page)

    # THEN
    with allure.step('Should sort rating'):
        main_page.should_page_movies_and_filter_and_sort(main_page)
