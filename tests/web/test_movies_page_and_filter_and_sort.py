from diploma_project.pages import page_open
import allure


def test_movies_page_and_filter():
    # GIVEN
    with allure.step('Открытие стартовой страницы'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Переход в меню фильмы'):
        main_page.open_page(main_page, 'Фильмы')
    with allure.step('Фильтрация фильмов по 2023 году и сортировка по рейтингу'):
        main_page.to_do_filtring_and_sorting(main_page)

    # THEN
    with allure.step('Проверка сортировки фильмов по рейтингу'):
        main_page.should_page_movies_and_filter_and_sort(main_page)
