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


def test_test():
    with step("Set heads"):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361',}
    with step("Set url"):
        url = "https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens"
    with step("Set payload"):
        payload = {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "rDZGI44TquVozSNB2rgXy"}
    with step("Run post request"):
        result = requests.post( url, headers=headers, json=payload)
    with step("Get id_session"):
        session_id = result.json()['session_id']

    with step("Load json schema"):
        schema = load_schema("get_moekino.json")

    with step("Set url"):
        url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/moekino?limit=1&offset=1'
    with step("Set heads"):
        headers = {'session_id': session_id,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
    with step("Run get request"):
        result = requests.get(url, headers=headers)

    with step("Assert status_code"):
        assert result.status_code == 200
    with step("Assert json schema"):
        jsonschema.validate(result.json(), schema)
    with step("Assert json_value name"):
        assert result.json()['name'] == 'Моё кино'
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")


