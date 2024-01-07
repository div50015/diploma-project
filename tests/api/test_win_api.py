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


def test_wink_my_movies():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361',}
    url = "https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens"
    payload = {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "rDZGI44TquVozSNB2rgXy"}
    result = requests.post( url, headers=headers, json=payload)
    session_id = result.json()['session_id']

    schema = load_schema("get_moekino.json")

    url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/moekino?limit=1&offset=1'
    headers = {'session_id': session_id,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
    result = requests.get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'Моё кино'


def test_wink_movies():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361',}
    url = "https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens"
    payload = {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "rDZGI44TquVozSNB2rgXy"}
    result = requests.post( url, headers=headers, json=payload)
    session_id = result.json()['session_id']

    schema = load_schema("get_kino.json")

    url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/movies?limit=1&offset=1'
    headers = {'session_id': session_id,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
    result = requests.get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'Фильмы'

def test_wink_serials():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361',}
    url = "https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens"
    payload = {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "rDZGI44TquVozSNB2rgXy"}
    result = requests.post( url, headers=headers, json=payload)
    session_id = result.json()['session_id']

    schema = load_schema("get_serials.json")

    url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/series?limit=1&offset=1'
    headers = {'session_id': session_id,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
    result = requests.get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['name'] == 'Сериалы'


def test_wink_tv_channels():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361',}
    url = "https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens"
    payload = {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "rDZGI44TquVozSNB2rgXy"}
    result = requests.post( url, headers=headers, json=payload)
    session_id = result.json()['session_id']

    schema = load_schema("get_tv_channels.json")

    url ='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/channels?with_epg=true&epg_limit=1&limit=1&offset=1'
    headers = {'session_id': session_id,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
    result = requests.get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['items'][0]['name'] == 'Всё ТВ'


# curl -u "igor_CuZE0R:oDYnn9pctxee3f5pAvwN" -X POST "https://api-cloud.browserstack.com/app-automate/upload"  -F "file=@C:\QA\Wink137100.apk"
# {"app_url":"bs://3373ebba06cc0797964d5c64bcf72aab147092cf"}

# logging.info(result.request.url)
# logging.info(result.request.headers)
# logging.info(result.request.body)
# logging.info(result.request.method)
