import time
from selene import browser, have, by
import os
from selene import command
from diploma_project.pages import main_page


def test_movies_page_and_filter():
    page = main_page.MainPage
    page.open_main_page(page)
    page.open_page(page,'Фильмы')
    page.should_movies_and_filter(page,'Все фильмы 2023 года')
