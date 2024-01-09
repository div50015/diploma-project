import time
from selene import browser, have, by
import os
from selene import command
from diploma_project.pages import page_open
import allure


def test_main_page():
    # GIVEN
    main_page = page_open.MainPage

    # WHEN
    with allure.step('Открытие стартовой страницы'):
        main_page.open_main_page(main_page)

    # THEN
    with allure.step('Проверка стартовой страницы'):
        main_page.should_main_page(main_page)

