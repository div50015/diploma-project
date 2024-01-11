import requests
import json
from diploma_project.utils.utils import load_schema
import jsonschema
from diploma_project.api import open_api
import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def test_serials(url_open, headers, payload, user_agent, url_serials):
    with step("Get session id"):
        headers_id = {
            'session_id': open_api.get_id(url_open, headers, payload),
            'user-agent': user_agent,
        }

    with step("Open page Serials"):
        result = requests.get(url_serials, headers=headers_id)

    with step("Should page Serials"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), load_schema("get_serials.json"))
        assert result.json()['name'] == 'Сериалы'

        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
