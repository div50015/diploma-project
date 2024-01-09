from diploma_project.pages import page_open
import allure


def test_movies_page():
    # GIVEN
    with allure.step('Открытие стартовой страницы'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Переход в меню сериалы'):
        main_page.open_page(main_page, 'Сериалы')

    # THEN
    with allure.step('Проверка страницы сериалы'):
        main_page.should_page_serials(main_page, 'Сериалы')



