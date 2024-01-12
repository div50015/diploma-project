import requests
import json
from diploma_project.utils.utils import load_schema
import jsonschema
from diploma_project.api import open_api
import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType


@allure.epic('API')
@allure.issue("https://jira.autotests.cloud/browse/HOMEWORK-1047", "HOMEWORK-1047")
@allure.story('my movies')
@allure.label('div50015', 'allure8')
@allure.tag('mobile')
def test_my_movies(url_open, headers, payload, user_agent, url_my_movies):
    with step("Get session id"):
        headers_id = {
            'session_id': open_api.get_id(url_open, headers, payload),
            'user-agent': user_agent,
        }

    with step("Get page My Movies"):
        result = requests.get(url_my_movies, headers=headers_id)

    with step("Should page My Movies"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), load_schema("get_moekino.json"))
        assert result.json()['name'] == 'Моё кино'

        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
