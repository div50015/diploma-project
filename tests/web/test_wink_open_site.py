import time
from selene import browser, have
import os
from selene import command


def test_open_site():
    browser.open('/')
    browser.all('nav').first.all('div a span').should(have.size(13))
    (browser.all('nav').first.all('div a span').should(have.exact_texts(
        'Главная', 'ТВ-каналы', 'Моё кино', 'Фильмы', 'Сериалы', 'Детям', 'Спорт', 'Блог')))

def test_page_tv_channels():
    browser.open('/')
    browser.all('nav').first.all('div a span').element_by(have.text('ТВ-каналы')).click()
    browser.element('a.lltcpd8.ld9ti8i > span').should(have.text('ТВ-каналы'))

def test_page_my_movie():
    browser.open('/')
    browser.all('nav').first.all('div a span').element_by(have.text('Моё кино')).click()
    browser.element('div.r1o2hf9x > h2').should(have.text('Моё кино'))

def test_page_movies():
    browser.open('/')
    browser.all('nav').first.all('div a span').element_by(have.text('Фильмы')).click()
    browser.element('div.r1o2hf9x > h2').should(have.text('Фильмы'))

def test_page_serials():
    browser.open('/')
    browser.all('nav').first.all('div a span').element_by(have.text('Сериалы')).click()
    browser.element('div.r35fcff').should(have.text('Сериалы'))

def test_page_movies_selection_by_year():
    browser.open('/')
    browser.all('nav').first.all('div a span').element_by(have.text('Фильмы')).click()
    browser.element('div.rbzy7g5 > div > div:nth-child(2) > button').click()
    browser.element('div.r1bo5h80.f1xfyimt > button > span > svg').click()
    browser.element('li:nth-child(3) > button > div.r1lbxtse.r3qime3').click()
    browser.all('ul > li:nth-child(1) > div > label').second.click()
    browser.element('div.w1f2pf8l > button').click()
    browser.element('div.t141zerc > h1').should(have.text('Все фильмы 2023 года'))
#   time.sleep(5)


def test_page_movies_selection_by_year_sorting_by_reyting():
    browser.open('/')
    browser.all('nav').first.all('div a span').element_by(have.text('Фильмы')).click()
    browser.element('div.rbzy7g5 > div > div:nth-child(2) > button').click()
    browser.element('div.r1bo5h80.f1xfyimt > button > span > svg').click()
    browser.element('li:nth-child(3) > button > div.r1lbxtse.r3qime3').click()
    browser.all('ul > li:nth-child(1) > div > label').second.click()
    browser.element('div.w1f2pf8l > button').click()
    browser.element('span > button:nth-child(2) > span > svg').click()
    browser.element('label:nth-child(2) > span').click()
    time.sleep(5)
    vv = browser.all('div.r1se895.ccukme8.rz6f1rl > span')
    for v in vv:
        p = v.locate().text
        print(f'span = {p}')

#  ul > li:nth-child(5) > div > label > span > svg > rect:nth-child(2)