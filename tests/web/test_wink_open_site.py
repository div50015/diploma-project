import time
from selene import browser, have
import os
from selene import command


def test_open_site():
    browser.open('/')
    l=[]
    l = browser.all('nav').first.all('div a span')
    # for v in vv:
    #     p = v.locate().text
    #     print(f'span = {p}')
    print(l)

    # vv = browser.all('nav').first.all('div a span')[0].locate().text
    # print(f'\r\n count elements = {vv}')
    # browser.all('#i4ukg0g').element(have.text('movies')).should(have.text('Фильмы'))
#    time.sleep(5)

#    i1b7aq89 Фильмы  i4ukg0g #header > div > div > div.moyk7m > div > nav > div:nth-child(1) > a > span

#header > div > div > div.moyk7m > div > nav > div:nth-child(1) > a > span