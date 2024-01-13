from selene import browser, have


class MainPage:

    def open_main_page(self):
        browser.open('/')
        return self

    def should_main_page(self):
        browser.all('nav').first.all('div a span').should(have.size(13))
        (browser.all('nav').first.all('div a span').should(have.texts(
            'Главная', 'ТВ-каналы', 'Моё кино', 'Фильмы', 'Сериалы', 'Детям', 'Спорт', 'Блог', 'Аудиокниги', 'Подписки',
            'Видеоблоги')))
        return self

    def open_tv_page(self):
        browser.all('.r1lbxtse.t1tsgdg8.rjqy0lg')[1].click()
        return self

    def open_my_movies_page(self):
        browser.all('.r1lbxtse.t1tsgdg8.rjqy0lg')[2].click()
        return self

    def open_movies_page(self):
        browser.all('.r1lbxtse.t1tsgdg8.rjqy0lg')[3].click()
        return self

    def open_serials_page(self):
        browser.all('.r1lbxtse.t1tsgdg8.rjqy0lg')[4].click()
        return self

    def should_page_serials(self, name_page):
        browser.element('.r1lbxtse.tia8zbe.r1et8e7w').should(have.text(f'{name_page}'))
        return self

    def should_page_my_movies(self, name_page):
        browser.all('.r1lbxtse.rgh77k2').first.should(have.text(f'{name_page}'))
        return self

    def should_page_tv(self, name_page):
        browser.element('[data-test="channels-title"]').should(have.text(f'{name_page}'))
        return self

    def to_do_filtering(self):
        browser.element('[data-test="cookie-btn"]').click()
        browser.element('[data-test="media-items-filter-button"]').click()
        browser.element('[data-test="filter-open-years"]').click()
        browser.element('[data-test="2023 г."]').click()
        browser.element('[data-test="filters-show-result"]').click()
        return self

    def should_movies_and_filter(self, name_filter):
        browser.element('div.t141zerc > h1').should(have.text(f'{name_filter}'))
        return self

    def to_do_filtring_and_sorting(self):
        browser.element('[data-test="cookie-btn"]').click()
        browser.element('[data-test="media-items-filter-button"]').click()
        browser.element('[data-test="filter-open-years"]').click()
        browser.element('[data-test="2023 г."]').click()
        browser.element('[data-test="filters-show-result"]').click()
        browser.element('[data-test="media-items-list-sort-button"]').click()
        browser.element('[for="wink-descsort"]').click()
        return self

    def should_page_movies_and_filter_and_sort(self):
        lst = []
        browser.all('.r1lbxtse.t1kaz2zr.r193vcky').should(have.size(48))
        reitings = browser.all('.r1lbxtse.t1kaz2zr.r193vcky')
        for reiting in reitings:
            lst.append(reiting.locate().text)

        assert all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
        return self


main_page = MainPage()
