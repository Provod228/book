import pytest


@pytest.fixture(scope='function')
def test_url(request: None) -> str:
    return 'http://127.0.0.1:8000/'


@pytest.fixture(scope='function')
def test_book_data() -> dict:
    return {
        'id': 1,
        'title': 'test_title',
        'genre': 'test_genre',
        'summary': 'test_summary',
        'isbn': 'test_isbn',
        'language': 'test_language',
    }


@pytest.fixture(scope='function')
def test_count_data() -> dict:
    return {
       'num_books': 1,
       'num_instance': 1,
       'num_instance_available': 1,
       'num_author': 1,
    }


@pytest.fixture(scope='function')
def test_author_data() -> dict:
    return {
        'first_name': "test_first_name",
        'last_name': "test_last_name",
        'data_of_birth': "1234-01-01",
        'data_of_death': "1265-01-01",
    }


@pytest.fixture(scope='function')
def test_book_instance_data() -> dict:
    return {
        'status_display': 1,
        'imprint': "test_imprint",
        'id': 1,
        'status': "test_status",
    }

