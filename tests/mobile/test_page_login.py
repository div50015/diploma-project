import allure
from diploma_project.pages import login_page, start_page


@allure.epic('MOBILE')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.story('login')
@allure.label('div50015', 'allure8')
@allure.tag('mobile')
def test_login(context):
    # GIVEN
    allure.dynamic.parameter('context', context)
    start_page.go_main_page()

    # WHEN
    login_page.go_login()

    # THEN
    login_page.should_login()
