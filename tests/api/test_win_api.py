import time
from selene import browser, have
import os
from selene import command
import os
import requests
import json
import logging
from diploma_project.utils.utils import load_schema
import jsonschema

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361', }
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361'
URL = "https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens"
PAYLOAD = {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "rDZGI44TquVozSNB2rgXy"}


def test_wink_my_movies():
    result = requests.post( url=URL, headers=HEADERS, json=PAYLOAD)
    session_id = result.json()['session_id']

    schema = load_schema("get_moekino.json")

    url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/moekino?limit=1&offset=1'
    headers = {'session_id': session_id, 'user-agent': USER_AGENT,}
    result = requests.get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'Моё кино'


def test_wink_movies():
    result = requests.post( url=URL, headers=HEADERS, json=PAYLOAD)
    session_id = result.json()['session_id']

    schema = load_schema("get_kino.json")

    url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/movies?limit=1&offset=1'
    headers = {'session_id': session_id,'user-agent': USER_AGENT,}
    result = requests.get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'Фильмы'

def test_wink_serials():
    result = requests.post( url=URL, headers=HEADERS, json=PAYLOAD)
    session_id = result.json()['session_id']

    schema = load_schema("get_serials.json")

    url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/series?limit=1&offset=1'
    headers = {'session_id': session_id,'user-agent': USER_AGENT,}
    result = requests.get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'Сериалы'


def test_wink_tv_channels():
    result = requests.post( url=URL, headers=HEADERS, json=PAYLOAD)
    session_id = result.json()['session_id']

    schema = load_schema("get_tv_channels.json")

    url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/channels?with_epg=true&epg_limit=1&limit=1&offset=1'
    headers = {'session_id': session_id,'user-agent': USER_AGENT,}
    result = requests.get(url, headers=headers)

    assert result.status_code == 200
    # jsonschema.validate(result.json(), schema)
    assert result.json()['items'][0]['name'] == 'Всё ТВ'


# logging.info(result.request.url)
# logging.info(result.request.headers)
# logging.info(result.request.body)
# logging.info(result.request.method)
