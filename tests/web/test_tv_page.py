from diploma_project.pages import page_open
import allure


def test_tv_page():
    # GIVEN
    with allure.step('Открытие стартовой страницы'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Переход в меню фильмы'):
        main_page.open_page(main_page,'Сериалы')

    # THEN
    with allure.step('Проверка страницы фильмы'):
        main_page.should_page_serials(main_page,'Сериалы')

