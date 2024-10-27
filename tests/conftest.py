import pytest
from django.urls import reverse
from catalog.models import Book, Author
from django.contrib.auth.models import User


@pytest.fixture(scope='function')
def test_url(request) -> str:
    return 'http://127.0.0.1:8000/'
