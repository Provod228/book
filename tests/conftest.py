import pytest
from django.test import Client
from catalog.models import Book, Author


pytest_plugins = "pytest_django"


@pytest.fixture(scope='function')
def main_url(request) -> str:
    return 'http://127.0.0.1:8000/'


@pytest.fixture(name="get_db")
def db(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        book1 = Book.objects.create(title='Золотой телёнок', isbn='978-5-389-135')
        author1 = Author.objects.create(first_name='Илья', last_name="Ильф")
        book1.author.add(author1)

        book2 = Book.objects.create(title='Война и мир', isbn='978-5-17-1181')
        author2 = Author.objects.create(first_name='Лев', last_name="Толстой")
        book2.author.add(author2)

    db_config = django_db_setup.db_config
    test_db_name = db_config['NAME']
    return test_db_name


@pytest.fixture
def session_db(db):
    return [
        Book.objects.all(),
        Book.objects.all(),
    ]
