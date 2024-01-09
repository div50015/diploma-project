import time
from selene import browser, have, by
import os
from selene import command
from diploma_project.pages import main_page


def test_my_movies_page():
    page = main_page.MainPage
    page.open_main_page(page)
    page.open_page(page,'Моё кино')
    page.should_page(page,'Моё кино')

