#  Дипломный проект по автоматизации тестирования сайта и мобильного приложения WINK 
> <a target="_blank" href="https://www.wink.ru">ссылка на сайт WINK</a>

![main page screenshot](pictures/screenshots/wink_web.png)

----

### Список UI автотестов

- [x] Главная страница отображается
- [x] Страница ТВ-каналы отображается
- [x] Страница Фильмы отображается 
- [x] Страница Моё кино отображается
- [x] Страница Сериалы отображается
- [x] Страница Фильмы с фильтром по 2023 году отображается
- [x] Страница Фильмы с фильтром и сортировкой по рейтингу отображается


### Список API автотестов

- [x] Страница авторизации отображается
- [x] Страница авторизации отображается
- [x] Страница поиска отображается
- [x] Страница Фильмы отображается


### Список MOBILE автотестов

- [x] Загрузка страницы Фильмы
- [x] Загрузка страницы Моё кино
- [x] Загрузка страницы Сериалы
- [x] Загрузка страницы ТВ-каналы

----

### Используемый стэк

<img title="Python" src="./pictures/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="./pictures/icons/pytest-original.svg" height="40" width="40"/> <img title="Pycharm" src="./pictures/icons/pycharm.png" height="40" width="40"/> <img title="Selenium" src="./pictures/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="./pictures/icons/selene.png" height="40" width="40"/> <img title="GitHub" src="./pictures/icons/github-original.svg" height="40" width="40"/> <img title="Allure Report" src="./pictures/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="./pictures/icons/AllureTestOps.png" height="40" width="40"/><img title="Telegram" src="./pictures/icons/tg.png" height="40" width="40"/><img title="Jira" src="./pictures/icons/jira-original.svg" height="40" width="40"/> 

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

![allure_report_overview](pictures/screenshots/allure-all-report.png)

#### Список тест кейсов

![allure_reports_behaviors](pictures/screenshots/allure-list-test.png)

#### Отчет прохождения теста

![allure_reports_graphs](pictures/screenshots/allure-test.png)


----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3941/launches">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](pictures/screenshots/testops-dashboard.png)

#### История запуска тестовых наборов

![allure_testops_launches](pictures/screenshots/testops-launches.png)

#### Тест кейсы

![allure_testops_suites](pictures/screenshots/testops-all-test.png)

----



### Оповещения в Telegram

<img src="./pictures/screenshots/tbot.png" width="300">
----

### Видео прохождения автотестов

![autotest_gif](pictures/video/ui1.gif)
<img src="./pictures/video/mobile1.gif" width="200">

----
#### Интеграция с JIRA

![allure_testops_suites](pictures/screenshots/jira-int.png)

----

