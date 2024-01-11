from selene import browser, be, have, query
import time


class MainPage:

    def open_main_page(self):
        browser.open('/')
        return self

    def should_main_page(self):
        browser.all('nav').first.all('div a span').should(have.size(13))
        (browser.all('nav').first.all('div a span').should(have.texts(
            'Главная', 'ТВ-каналы', 'Моё кино', 'Фильмы', 'Сериалы', 'Детям', 'Спорт', 'Блог', 'Аудиокниги',
            'Подписки')))
        return self

    def open_page(self, name_page):
        browser.all('nav').first.all('div a span').element_by(have.text(f'{name_page}')).click()
        return self

    def should_page(self, name_page):
        browser.element('div.r1o2hf9x > h2').should(have.text(f'{name_page}'))
        return self

    def should_page_my_movies(self, name_page):
        browser.element('div:nth-child(2) > div > div.r1o2hf9x > h3').should(have.text(f'{name_page}'))
        return self

    def should_page_serials(self, name_page):
        browser.element('div.r35fcff').should(have.text(f'{name_page}'))
        return self

    def should_page_tv(self, name_page):
        browser.element('a.lltcpd8.ld9ti8i > span').should(have.text(f'{name_page}'))
        return self

    def to_do_filtering(self):
        browser.element('div.rbzy7g5 > div > div:nth-child(2) > button').click()
        browser.element('div.r1bo5h80.f1xfyimt > button > span > svg').click()
        browser.element('li:nth-child(3) > button > div.r1lbxtse.r3qime3').click()
        browser.all('ul > li:nth-child(1) > div > label').second.click()
        browser.element('div.w1f2pf8l > button').click()
        return self

    def should_movies_and_filter(self, name_filter):
        browser.element('div.t141zerc > h1').should(have.text(f'{name_filter}'))
        return self

    def to_do_filtring_and_sorting(self):
        browser.element('div.rbzy7g5 > div > div:nth-child(2) > button').click()
        browser.element('div.r1bo5h80.f1xfyimt > button > span > svg').click()
        browser.element('li:nth-child(3) > button > div.r1lbxtse.r3qime3').click()
        browser.all('ul > li:nth-child(1) > div > label').second.click()
        browser.element('div.w1f2pf8l > button').click()
        browser.element('span > button:nth-child(2) > span > svg').click()
        browser.element('label:nth-child(2) > span').click()
        time.sleep(5)
        return self

    def should_page_movies_and_filter_and_sort(self):
        lst = []
        reitings = browser.all('div.r1se895.ccukme8.rz6f1rl > span')
        for reiting in reitings:
            lst.append(reiting.locate().text)
            # print(f'span = {lst}')

        assert all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
        return self
