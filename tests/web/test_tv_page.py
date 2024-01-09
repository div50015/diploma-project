import time
from selene import browser, have, by
import os
from selene import command
from diploma_project.pages import main_page


def test_tv_page():
    page = main_page.MainPage
    page.open_main_page(page)
    page.open_page(page,'Сериалы')
    page.should_page_serials(page,'Сериалы')

