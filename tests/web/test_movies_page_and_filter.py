from diploma_project.pages import page_open
import allure


def test_movies_page_and_filter():
    # GIVEN
    with allure.step('Открытие стартовой страницы'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Переход в меню фильмы'):
        main_page.open_page(main_page,'Фильмы')

    with allure.step('Фильтрация фильмов по 2023 году'):
        main_page.to_do_filtering(main_page)

    # THEN
    with allure.step('Проверка страницы фильмы c фильтрацией по 2023 году'):
        main_page.should_movies_and_filter(main_page,'Все фильмы 2023 года')


# def test_movies_page():
#     # GIVEN
#     with allure.step('Открытие стартовой страницы'):
#         main_page = page_open.MainPage
#         main_page.open_main_page(main_page)
#
#     # WHEN
#     with allure.step('Переход в меню фильмы'):
#         main_page.open_page(main_page, 'Фильмы')
#
#     # THEN
#     with allure.step('Проверка страницы фильмы'):
#         main_page.should_page(main_page, 'Фильмы')
