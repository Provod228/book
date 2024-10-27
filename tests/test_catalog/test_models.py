import pytest
import requests
from catalog.models import *
import datetime


@pytest.mark.django_db
def test_models_in_db():
    book = Book.objects.create(
        title='Золотой телёнок',
        isbn='978-5-389-135',
        summary='«Золото́й телёнок» — сатирический роман Ильи Ильфа и Евгения Петрова,'
                ' завершённый в 1931 году. В основе сюжета — дальнейшие приключения центрального '
                'персонажа «Двенадцати стульев» Остапа Бендера, происходящие на фоне картин'
                ' советской жизни начала 1930-х годов, а именно Первой пятилетки.'
                ' Роман перекликается с рядом произведений русской и зарубежной литературы[⇨].'
                ' В числе художественных приёмов, используемых соавторами, — гипербола, гротеск, каламбур, пародия.',
        genre=Genre.objects.create(name='Приключения'),
        language=Language.objects.create(name='Русский'),
    )
    author1 = Author.objects.create(
        first_name='Илья',
        last_name="Ильф",
        data_of_birth='1897-10-15',
        data_of_death='1937-04-13',
    )
    author2 = Author.objects.create(
        first_name='Евгений',
        last_name="Петров",
        data_of_birth='1903-12-13',
        data_of_death='1942-07-02',
    )
    status = Status.objects.create(name='Склад')
    book_instance = BookInstance.objects.create(
        imprint='REE',
        due_back='2023-01-02',
        inv_nom='F3125tewf',
        book=book,
        status=status,
    )
    book.author.add(author1)
    book.author.add(author2)
    assert BookInstance.objects.get(status=1).status.name == 'Склад'
    assert BookInstance.objects.get(book=1).imprint == 'REE'
    assert 'Золотой телёнок' in Book.objects.get(title='Золотой телёнок').title
    assert Book.objects.get(title='Золотой телёнок').author.count() == 2
    assert Book.objects.get(title='Золотой телёнок').genre.id == 1
    assert Book.objects.get(title='Золотой телёнок').language.id == 1
    assert (Author.objects.get(first_name='Илья', last_name="Ильф").data_of_birth ==
            datetime.date(1897, 10, 15))
    assert (Author.objects.get(first_name='Илья', last_name="Ильф").data_of_death ==
            datetime.date(1937, 4, 13))
