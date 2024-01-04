import time
from selene import browser, have
import os
from selene import command


def test_open_site():
    browser.open('/')
    browser.all('nav').first.all('div a span').should(have.size(13))
    (browser.all('nav').first.all('div a span').
     should(have.
    exact_texts('Главная', 'ТВ-каналы', 'Моё кино', 'Фильмы', 'Сериалы', 'Детям', 'Спорт', 'Блог')))
    # for v in vv:
    #     p = v.locate().text
    #     print(f'span = {p}')
    # vv = browser.all('nav').first.all('div a span')[0].locate().text
    # print(f'\r\n count elements = {vv}')
    # browser.all('#i4ukg0g').element(have.text('movies')).should(have.text('Фильмы'))
    # time.sleep(5)

def test_page_movies():
    browser.open('/')
    browser.all('nav').first.all('div a span').element(have.text('ТВ-каналы')).click()
    browser.all('main span').should(have.text('ТВ-каналы'))

#header > div > div > div.moyk7m > div > nav > div:nth-child(2) > a > span
#root > div.rwh68sa > div.r15qqrn5 > main > div > div > div.r1iu6vdu.zujqyi9 > div > a.lltcpd8.ld9ti8i > span