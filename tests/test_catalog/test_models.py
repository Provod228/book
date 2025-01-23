import pytest
from catalog.models import Genre, Language, Book, Author, Status, BookInstance
from catalog.factories import (
    GenreFactory,
    LanguageFactory,
    AuthorFactory,
    StatusFactory,
    BookFactory,
    BookInstanceFactory,
)
import datetime
import factory


@pytest.mark.django_db
def test_model_book_instance(test_book_instance_factory: BookInstanceFactory) -> None:
    factory_book = test_book_instance_factory
    book: str = factory_book.book
    inv_nom: int = factory_book.inv_nom
    imprint: str = factory_book.imprint
    status: str = factory_book.status
    due_back: datetime.datetime = factory_book.due_back

    assert len(str(inv_nom)) <= 20
    assert len(imprint) <= 200
    assert isinstance(book, Book)
    assert isinstance(inv_nom, int)
    assert isinstance(imprint, str)
    assert isinstance(status, Status)
    assert isinstance(due_back, datetime.datetime)


@pytest.mark.django_db
def test_model_book(test_book_factory: BookFactory) -> None:
    title: str = test_book_factory.title
    genre: Genre = test_book_factory.genre
    language: Language = test_book_factory.language
    summary: str = test_book_factory.summary
    isbn: str = test_book_factory.isbn
    authors: QuerySet = test_book_factory.author.all()

    print(type(authors))
    assert len(summary) <= 1000
    assert len(title) <= 200
    assert len(isbn) <= 13
    assert isinstance(title, str)
    assert isinstance(genre, Genre)
    assert isinstance(language, Language)
    assert isinstance(summary, str)
    assert isinstance(isbn, str)

    for author in authors:
        assert isinstance(author, Author)


@pytest.mark.django_db
def test_model_author(test_author_factory: AuthorFactory) -> None:
    first_name: str = test_author_factory.first_name
    last_name: str = test_author_factory.last_name
    data_of_birth: datetime.datetime = test_author_factory.data_of_birth
    data_of_death: datetime.datetime = test_author_factory.data_of_death

    assert len(first_name) <= 100
    assert len(last_name) <= 100
    assert isinstance(first_name, str)
    assert isinstance(last_name, str)
    assert isinstance(data_of_birth, datetime.datetime)
    assert isinstance(data_of_death, datetime.datetime)


@pytest.mark.django_db
def test_model_status(test_status_factory: StatusFactory) -> None:
    name: str = test_status_factory.name

    assert len(name) <= 20
    assert isinstance(name, str)


@pytest.mark.django_db
def test_model_genre(test_genre_factory: GenreFactory) -> None:
    name: str = test_genre_factory.name

    assert len(name) <= 200
    assert isinstance(name, str)


@pytest.mark.django_db
def test_model_language(test_language_factory: LanguageFactory) -> None:
    name: str = test_language_factory.name

    assert len(name) <= 20
    assert isinstance(name, str)
