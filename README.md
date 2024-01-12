#  Дипломный проект по автоматизации тестирования сайта и мобильного приложения WINK 
> <a target="_blank" href="https://www.wink.ru">ссылка на сайт WINK</a>

![main page screenshot](./pictures/wink_web.png)

----

### Список проверок, реализованных в UI автотестах

- [x] Главная страница отображается
- [x] Страница ТВ-каналы отображается
- [x] Страница Фильмы отображается 
- [x] Страница Моё кино отображается
- [x] Страница Сериалы отображается
- [x] Страница Фильмы с фильтром по 2023 году отображается
- [x] Страница Фильмы с фильтром и сортировкой по рейтингу отображается


### Список проверок, реализованных в API автотестах

- [x] Страница авторизации отображается
- [x] Страница авторизации отображается
- [x] Списание поиска отображается
- [x] Списание Фильмы отображается


### Список проверок, реализованных в MOBILE автотестах

- [x] Загрузка страницы Фильмы
- [x] Загрузка страницы Моё кино
- [x] Загрузка страницы Сериалы
- [x] Загрузка страницы ТВ-каналы

----

### Используемый стэк

<img title="Python" src="./pictures/python-original.svg" height="40" width="40"/> <img title="Pytest" src="./pictures/pytest-original.svg" height="40" width="40"/> <img title="Pycharm" src="./pictures/pycharm.png" height="40" width="40"/> <img title="Selenium" src="./pictures/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="./pictures/selene.png" height="40" width="40"/> <img title="GitHub" src="./pictures/github-original.svg" height="40" width="40"/> <img title="Allure Report" src="./pictures/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="./pictures/AllureTestOps.png" height="40" width="40"/><img title="Telegram" src="./pictures/tg.png" height="40" width="40"/><img title="Jira" src="./pictures/jira-original.svg" height="40" width="40"/> 

----

### Локальный запуск автотестов

#### Выполнить в cli:
> [!NOTE]
> Ключ выбора версии `--browser-version` не обязателен

> [!NOTE]
> Ключ выбора мобильного устройства `--context` не обязателен
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser-version=100 --context=bstack
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C08_div50015_diploma1//">Ссылка</a>

#### Параметры сборки


* environment - параметр определяет окружение для запуска тестов
* comment - комментарий


#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/lesson15-hw_jenkins_full_project//">проект</a>
2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать: PROD
4. В поле "COMMENT" ввести комментарий
5. Нажать "Build"

----

### Allure отчет
#### Общие результаты

![allure_report_overview](./pictures/allure-all-report.png)

#### Список тест кейсов

![allure_reports_behaviors](./pictures/allure-list-test.png)

#### Отчет прохождения теста

![allure_reports_graphs](./pictures/allure-test.png)


----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3941/launches">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](./pictures/testops-dashboard.png)

#### История запуска тестовых наборов

![allure_testops_launches](./pictures/testops-launches.png)

#### Тест кейсы

![allure_testops_suites](./pictures/testops-all-test.png)

----



### Оповещения в Telegram

![telegram_allert](./pictures/tbot.png)

----

### Видео прохождения автотестов

![autotest_gif](./pictures/ui1.gif)
<img src="./pictures/mobile1.gif" width="200">
----

