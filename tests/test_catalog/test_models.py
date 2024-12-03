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
    book: str = test_book_instance_factory.book
    inv_nom: int = test_book_instance_factory.inv_nom
    imprint: str = test_book_instance_factory.imprint
    status: str = test_book_instance_factory.status
    due_back: datetime.datetime = test_book_instance_factory.due_back

    assert type(book) is Book
    assert type(inv_nom) is int
    assert type(imprint) is str
    assert type(status) is Status
    assert type(due_back) is datetime.datetime


@pytest.mark.django_db
def test_model_book(test_book_factory: BookFactory) -> None:
    title: str = test_book_factory.title
    genre: str = test_book_factory.genre
    language: str = test_book_factory.language
    summary: str = test_book_factory.summary
    isbn: str = test_book_factory.isbn
    author: str = test_book_factory.author

    assert type(title) is str
    assert type(genre) is Genre
    assert type(language) is Language
    assert type(summary) is str
    assert type(isbn) is str
    assert type(author) is not Author


@pytest.mark.django_db
def test_model_author(test_author_factory: AuthorFactory) -> None:
    first_name: factory.faker.Faker = AuthorFactory.first_name
    last_name: factory.faker.Faker = AuthorFactory.last_name
    data_of_birth: factory.faker.Faker = AuthorFactory.data_of_birth
    data_of_death: factory.faker.Faker = AuthorFactory.data_of_death

    assert type(first_name) is factory.faker.Faker
    assert type(last_name) is factory.faker.Faker
    assert type(data_of_birth) is factory.faker.Faker
    assert type(data_of_death) is factory.faker.Faker


@pytest.mark.django_db
def test_model_status(test_status_factory: StatusFactory) -> None:
    name: str = test_status_factory.name

    assert type(name) is str


@pytest.mark.django_db
def test_model_genre(test_genre_factory: GenreFactory) -> None:
    name: str = test_genre_factory.name

    assert type(name) is str


@pytest.mark.django_db
def test_model_language(test_language_factory: LanguageFactory) -> None:
    name: str = test_language_factory.name

    assert type(name) is str


# @pytest.mark.django_db
# def test_models_in_db() -> None:
#     genre = Genre.objects.create(name='Приключения')
#     language = Language.objects.create(name='Русский')
#     book = Book.objects.create(
#         title='Золотой телёнок',
#         isbn='978-5-389-135',
#         summary='«Золото́й телёнок» — сатирический роман Ильи Ильфа и Евгения Петрова,'
#                 ' завершённый в 1931 году. В основе сюжета — дальнейшие приключения центрального '
#                 'персонажа «Двенадцати стульев» Остапа Бендера, происходящие на фоне картин'
#                 ' советской жизни начала 1930-х годов, а именно Первой пятилетки.'
#                 ' Роман перекликается с рядом произведений русской и зарубежной литературы[⇨].'
#                 ' В числе художественных приёмов, используемых соавторами, — гипербола, гротеск, каламбур, пародия.',
#         genre=genre,
#         language=language,
#     )
#     author1 = Author.objects.create(
#         first_name='Илья',
#         last_name="Ильф",
#         data_of_birth='1897-10-15',
#         data_of_death='1937-04-13',
#     )
#     author2 = Author.objects.create(
#         first_name='Евгений',
#         last_name="Петров",
#         data_of_birth='1903-12-13',
#         data_of_death='1942-07-02',
#     )
#     status = Status.objects.create(name='Склад')
#     book_instance = BookInstance.objects.create(
#         imprint='REE',
#         due_back='2023-01-02',
#         inv_nom='F3125tewf',
#         book=book,
#         status=status,
#     )
#     book.author.add(author1)
#     book.author.add(author2)
#     assert BookInstance.objects.get(status=1).status.name == 'Склад'
#     assert BookInstance.objects.get(book=1).imprint == 'REE'
#     assert 'Золотой телёнок' in Book.objects.get(title='Золотой телёнок').title
#     assert Book.objects.get(title='Золотой телёнок').author.count() == 2
#     assert Book.objects.get(title='Золотой телёнок').genre.id == 1
#     assert Book.objects.get(title='Золотой телёнок').language.id == 1
#     assert (Author.objects.get(first_name='Илья', last_name="Ильф").data_of_birth ==
#             datetime.date(1897, 10, 15))
#     assert (Author.objects.get(first_name='Илья', last_name="Ильф").data_of_death ==
#             datetime.date(1937, 4, 13))
