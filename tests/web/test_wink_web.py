import time
from selene import browser, have, by
import os
from selene import command
from diploma_project.pages import page_open
# def test_page_login():
#     browser.open('/')
#     time.sleep(1)
#     browser.element('div.bwx50sy > div > button').click()
#     time.sleep(1)
#     browser.element('li:nth-child(1) > button').click()
#     time.sleep(1)
#     browser.element('li:nth-child(1) > button').click()
#     time.sleep(1)
# #    browser.element('div.tn1c75m > h3').should(have.text(''))
#
#  browser.element('div.rbzy7g5 > div > div:nth-child(2) > button').




# def test_open_site():
#     browser.open('/')
#     browser.all('nav').first.all('div a span').should(have.size(13))
#     (browser.all('nav').first.all('div a span').should(have.texts(
#         'Главная', 'ТВ-каналы', 'Моё кино', 'Фильмы', 'Сериалы', 'Детям', 'Спорт', 'Блог', 'Аудиокниги', 'Подписки')))
#
#
#
# def test_page_tv_channels():
#     browser.open('/')
#     browser.all('nav').first.all('div a span').element_by(have.text('ТВ-каналы')).click()
#     browser.element('a.lltcpd8.ld9ti8i > span').should(have.text('ТВ-каналы'))
#
# def test_page_my_movie():
#     browser.open('/')
#     browser.all('nav').first.all('div a span').element_by(have.text('Моё кино')).click()
#     browser.element('div.r1o2hf9x > h2').should(have.text('Моё кино'))
#
# def test_page_movies():
#     browser.open('/')
#     browser.all('nav').first.all('div a span').element_by(have.text('Фильмы')).click()
#     browser.element('div.r1o2hf9x > h2').should(have.text('Фильмы'))
#
# def test_page_serials():
#     browser.open('/')
#     browser.all('nav').first.all('div a span').element_by(have.text('Сериалы')).click()
#     browser.element('div.r35fcff').should(have.text('Сериалы'))
#
# def test_page_movies_selection_by_year():
#     browser.open('/')
#     browser.all('nav').first.all('div a span').element_by(have.text('Фильмы')).click()
#     browser.element('div.rbzy7g5 > div > div:nth-child(2) > button').click()
#     browser.element('div.r1bo5h80.f1xfyimt > button > span > svg').click()
#     browser.element('li:nth-child(3) > button > div.r1lbxtse.r3qime3').click()
#     browser.all('ul > li:nth-child(1) > div > label').second.click()
#     browser.element('div.w1f2pf8l > button').click()
#     browser.element('div.t141zerc > h1').should(have.text('Все фильмы 2023 года'))
# #   time.sleep(5)
#
#
# def test_page_movies_selection_by_year_sorting_by_reyting():
#     browser.open('/')
#     browser.all('nav').first.all('div a span').element_by(have.text('Фильмы')).click()
#     browser.element('div.rbzy7g5 > div > div:nth-child(2) > button').click()
#     browser.element('div.r1bo5h80.f1xfyimt > button > span > svg').click()
#     browser.element('li:nth-child(3) > button > div.r1lbxtse.r3qime3').click()
#     browser.all('ul > li:nth-child(1) > div > label').second.click()
#     browser.element('div.w1f2pf8l > button').click()
#     browser.element('span > button:nth-child(2) > span > svg').click()
#     browser.element('label:nth-child(2) > span').click()
#     time.sleep(5)
#     lst = []
#     reitings = browser.all('div.r1se895.ccukme8.rz6f1rl > span')
#     for reiting in reitings:
#         lst.append(reiting.locate().text)
#         # print(f'span = {lst}')
#
#     assert all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
# #  ul > li:nth-child(5) > div > label > span > svg > rect:nth-child(2)