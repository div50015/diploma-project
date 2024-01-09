from diploma_project.pages import page_open
import allure


def test_my_movies_page():
    # GIVEN
    with allure.step('Открытие стартовой страницы'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Переход в меню моё кино'):
        main_page.open_page(main_page, 'Моё кино')

    # THEN
    with allure.step('Проверка страницы моё кино'):
        main_page.should_page(main_page, 'Моё кино')
