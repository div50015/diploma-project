import time
from selene import browser, have, by
import os
from selene import command
from diploma_project.pages import page_open
import allure


@allure.epic('UI')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.feature('Страницы')
@allure.story('main')
@allure.label('div50015', 'allure8')
@allure.tag('ui')
def test_main_page():
    # GIVEN
    with allure.step('Opening main page'):
        main_page = page_open.MainPage
        main_page.open_main_page(main_page)


    # WHEN
    with allure.step('Opening main page'):
        main_page.open_main_page(main_page)

    # THEN
    with allure.step('Should main page'):
        main_page.should_main_page(main_page)

