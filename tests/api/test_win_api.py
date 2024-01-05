import time
from selene import browser, have
import os
from selene import command
import os
import requests
import json

def test_wink_movies():
    browser.open('/')

    # result = requests.post(
    #     url=API_URL + '/addproducttocart/details/22/1',
    #     data={'addtocart_22.EnteredQuantity': 1},
    #     cookies={"NOPCOMMERCE.AUTH": cookie}
    # )
    session_id = browser.driver.session_id
    print(f'\r\n   session_id = {session_id}')
    # result = requests.get(url='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/movies?limit=4&offset=0',
    result = requests.get(url='https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v3/user/media_views/alias/movies',
                          headers={'session_id': "939c5522-ab8c-11ee-94f6-f063f976f34d:1951421:99863903:8"},
                          # params={'limit': '4', 'offset': '0'},
                          )
    assert result.status_code == 200
    time.sleep(2)