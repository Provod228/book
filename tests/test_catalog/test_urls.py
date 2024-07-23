import pytest
import requests
import catalog.models as model
'''Тестировать при запуске сайта'''


def test_index(test_url) -> None:
    url = test_url + 'catalog/'
    response = str(requests.get(url))
    assert response == '<Response [200]>'


def test_books(test_url) -> None:
    url = test_url + 'catalog/books/'
    response = str(requests.get(url))
    assert response == '<Response [200]>'


def test_authors(test_url) -> None:
    url = test_url + 'catalog/authors/'
    response = str(requests.get(url))
    assert response == '<Response [200]>'


def test_login(test_url) -> None:
    url = test_url + 'catalog/accounts/login/'
    response = str(requests.get(url))
    assert response == '<Response [200]>'
