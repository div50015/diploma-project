import allure
from diploma_project.mobile import start_page, movies_page


@allure.epic('MOBILE')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.story('movies')
@allure.label('div50015', 'allure8')
@allure.tag('mobile')
def test_movies(context):
    # GIVEN
    allure.dynamic.parameter('context', context)
    start_page.go_main_page()

    # WHEN
    movies_page.go_movies()

    # THEN
    movies_page.should_movies()
