import allure
from diploma_project.mobile import start_page


@allure.epic('MOBILE')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.story('main page')
@allure.label('div50015', 'allure8')
@allure.tag('mobile')
def test_start(context):
    # GIVEN
    allure.dynamic.parameter('context', context)

    # THEN
    start_page.shoult_page_one()
    start_page.go_next_page()
    start_page.shoult_page_two()
    start_page.go_next_page()
    start_page.shoult_page_three()
    start_page.go_next_page()
    start_page.shoult_page_four()
    start_page.go_next_page()
    start_page.shoult_page_five()
    start_page.go_past_page()
    start_page.should_main_page()
