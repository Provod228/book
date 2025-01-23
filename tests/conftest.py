import pytest
from catalog.factories import (
    GenreFactory,
    LanguageFactory,
    AuthorFactory,
    StatusFactory,
    BookFactory,
    BookInstanceFactory,
)


@pytest.fixture(scope='function')
def test_book_instance_factory() -> BookInstanceFactory:
    book_instance_create: BookInstanceFactory = BookInstanceFactory.create()
    return book_instance_create


@pytest.fixture(scope='function')
def test_book_factory() -> BookFactory:
    author1: AuthorFactory = AuthorFactory.create()
    author2: AuthorFactory = AuthorFactory.create()
    book_create: BookFactory = BookFactory.create(author__=[author1, author2])
    return book_create


@pytest.fixture(scope='function')
def test_author_factory() -> AuthorFactory:
    author_create: AuthorFactory = AuthorFactory.create()
    return author_create


@pytest.fixture(scope='function')
def test_status_factory() -> StatusFactory:
    status_create: StatusFactory = StatusFactory.create()
    return status_create


@pytest.fixture(scope='function')
def test_genre_factory() -> GenreFactory:
    genre_factory: GenreFactory = GenreFactory.create()
    return genre_factory


@pytest.fixture(scope='function')
def test_language_factory() -> LanguageFactory:
    language_factory: LanguageFactory = LanguageFactory.create()
    return language_factory


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

