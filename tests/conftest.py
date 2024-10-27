import pytest


@pytest.fixture(scope='function')
def test_url(request) -> str:
    return 'http://127.0.0.1:8000/'
