import requests
import json
from diploma_project.utils.utils import load_schema
import jsonschema
from diploma_project.api import open_api, menu_api
import allure
import logging
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def test_wink_my_movies():
    with step("Open page and get id session with API"):
        headers = {'session_id': open_api.open_api(), 'user-agent': open_api.USER_AGENT, }

    with step("Open page my movies with API"):
        result = requests.get(url=menu_api.URL_MY_MOVIES, headers=headers)

    with step("Should page my movies with API"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), load_schema("get_moekino.json"))
        assert result.json()['name'] == 'Моё кино'
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")


def test_wink_movies():
    with step("Open page and get id session with API"):
        headers = {'session_id': open_api.open_api(), 'user-agent': open_api.USER_AGENT, }

    with step("Open page movies with API"):
        result = requests.get(url=menu_api.URL_MOVIES, headers=headers)

    with step("Should page movies with API"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), load_schema("get_kino.json"))
        assert result.json()['name'] == 'Фильмы'
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")


def test_wink_serials():
    with step("Open page and get id session with API"):
        headers = {'session_id': open_api.open_api(), 'user-agent': open_api.USER_AGENT, }

    with step("Open page serials with API"):
        result = requests.get(url=menu_api.URL_SERIALS, headers=headers)

    with step("Should page serials with API"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), load_schema("get_serials.json"))
        assert result.json()['name'] == 'Сериалы'
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")


def test_wink_tv_channels():
    with step("Open page and get id session with API"):
        headers = {'session_id': open_api.open_api(), 'user-agent': open_api.USER_AGENT, }

    with step("Open page tv with API"):
        result = requests.get(url=menu_api.URL_TV, headers=headers)

    with step("Should page tv with API"):
        assert result.status_code == 200
        # jsonschema.validate(result.json(), load_schema("get_tv_channels.json"))
        assert result.json()['items'][0]['name'] == 'Всё ТВ'
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")

