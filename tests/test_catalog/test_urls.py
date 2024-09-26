import requests
'''Тестировать при запуске сайта'''


def test_url_index(main_url) -> None:
    url = main_url + 'catalog/'
    response = requests.get(url)
    assert response.status_code == 200


def test_url_books(main_url) -> None:
    url = main_url + 'catalog/books/'
    response = requests.get(url)
    assert response.status_code == 200


def test_url_authors(main_url) -> None:
    url = main_url + 'catalog/authors/'
    response = requests.get(url)
    assert response.status_code == 200


def test_url_login(main_url) -> None:
    url = main_url + 'catalog/accounts/login/'
    response = requests.get(url)
    assert response.status_code == 200


def test_book_ids(session_db):
    assert session_db[0] != session_db[1]
