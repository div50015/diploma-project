import requests

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361', }
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361'
URL = "https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/user/session_tokens"
PAYLOAD = {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "rDZGI44TquVozSNB2rgXy"}


def open_api():
    result = requests.post(url=URL, headers=HEADERS, json=PAYLOAD)
    return result.json()['session_id']
