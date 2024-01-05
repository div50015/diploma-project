import time
from selene import browser, have
import os
from selene import command
import os
import requests
import json
import logging

def test_wink_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Postman-Token': '8b0e3ec0-c5c5-41f1-8b1c-2b152ab2b581',
    }
    url = "https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens"
    payload = {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "Yc6iBwS6-aCvRbFGInW5p"}
    result = requests.post( url, headers=headers, json=payload)
    s_c1 = result.status_code
    print(f'\r\nstatus_code1 = {s_c1}')
    s_id = result.json()['session_id']
    print(f'session_id = {s_id}')

    sid1 = '5ee00cd5-ac06-11ee-94f6-f063f976f34d:1951421:99863903:8'
    sid = '735d8fa0-aa58-11ee-be92-f063f976f300:1951421:99863903:8'
    url = "https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/moekino?limit=4&offset=0"
    payload = {}
    # headers = {'session_id': '939c5522-ab8c-11ee-94f6-f063f976f34d:1951421:99863903:8', 'Host': 'cnt-m7-itv02.svc.iptv.rt.ru'}
    payload = {}
    headers = {
    'session_id': sid,
    # 'session_id': '735d8fa0-aa58-11ee-be92-f063f976f300:1951421:99863903:8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    result = requests.get(url, headers=headers, data=payload)

    s_c2 = result.status_code
    print(f'status_code2 = {s_c2}')

    s_name = result.json()['name']
    print(f'name = {s_name}')

    print(f'\r\nsid  =  {sid}')
    print(f's_id =  {s_id}')


# logging.info(result.request.url)
# logging.info(result.request.headers)
# logging.info(result.request.body)
# logging.info(result.request.method)
