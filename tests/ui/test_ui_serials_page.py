from diploma_project.pages import page_open
import allure


def test_movies_page():
    # GIVEN
    with allure.step('Opening main page'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)

    # WHEN
    with allure.step('Go to Serials page'):
        main_page.open_page(main_page, 'Сериалы')

    # THEN
    with allure.step('Should Serials page'):
        main_page.should_page_serials(main_page, 'Сериалы')
