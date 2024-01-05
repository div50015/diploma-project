import time
from selene import browser, have
import os
from selene import command
import os
import requests
import json
import logging

def test_wink_movies():
    # browser.open('/')
    # time.sleep(5)
    url = f'https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens'
    headers = {
        'Content-Type': 'text/plain',
        'Postman-Token': 'b389a695-f448-46fe-a69d-d163f775cd2b',
        'Host': 'cnt-odcv-itv01.svc.iptv.rt.ru',
        'Content-Length': '86'
    }
    data = {
        'device': {'type': 'NCWEB', 'platform': 'browser'},
        'fingerprint': 'rDZGI44TquVozSNB2rgXy'
    }
    result = requests.post(url=url, headers=headers, data=data)
    s_c = result.status_code
    print(f'\r\n   session_id = {s_c}')
    print('url')
    logging.info(result.request.url)
    print('headers')
    logging.info(result.request.headers)
    print('body')
    logging.info(result.request.body)

    # result = requests.get(
    #     url='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/movies',
    #     headers={'session_id': "939c5522-ab8c-11ee-94f6-f063f976f34d:1951421:99863903:8", 'Host': 'cnt-m7-itv02.svc.iptv.rt.ru'},
    #                       )
    # s_c = result.status_code
    # print(f'\r\n   session_id = {s_c}')
