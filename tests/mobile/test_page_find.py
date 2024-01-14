import allure
from diploma_project.pages import find_page, start_page


@allure.epic('MOBILE')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.story('find')
@allure.label('div50015', 'allure8')
@allure.tag('mobile')
def test_find(context):
    # GIVEH
    allure.dynamic.parameter('context', context)
    start_page.go_main_page()

    # WHEN
    find_page.go_find()

    # THEN
    find_page.should_find()
