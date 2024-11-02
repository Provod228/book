import requests
from requests.exceptions import RequestException
import pytest
'''Тестировать при запуске сайта'''


@pytest.mark.parametrize("endpoint", [
    'catalog/',
    'catalog/books/',
    'catalog/authors/',
    'catalog/accounts/login/',
])
def test_endpoints(test_url: str, endpoint: str) -> None:
    url = test_url + endpoint
    try:
        response = requests.get(url)
        assert response.status_code == 200
    except RequestException as e:
        assert False, f"Request failed: {e}"
