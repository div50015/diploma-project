import pytest


def url_api():
    return 'https://cnt-lbrc-itv01.svc.iptv.rt.ru'


@pytest.fixture
def url_open():
    return f'{url_api()}/api/v2/user/session_tokens'


@pytest.fixture
def url_my_movies():
    return f'{url_api()}/api/v3/user/media_views/alias/moekino?limit=1&offset=1'


@pytest.fixture
def url_movies():
    return f'{url_api()}/api/v3/user/media_views/alias/movies?limit=1&offset=1'


@pytest.fixture
def url_serials():
    return f'{url_api()}/api/v3/user/media_views/alias/series?limit=1&offset=1'


@pytest.fixture
def url_tv():
    return f'{url_api()}/api/v2/user/channels?with_epg=true&epg_limit=1&limit=1&offset=1'


@pytest.fixture
def headers():
    return {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361'}


@pytest.fixture
def user_agent():
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.361'


@pytest.fixture
def payload():
    return {"device": {"type": "NCWEB", "platform": "browser"}, "fingerprint": "rDZGI44TquVozSNB2rgXy"}
