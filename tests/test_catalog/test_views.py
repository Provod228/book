import pytest
from catalog.models import Author, Book, BookInstance
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.test import TestCase


@pytest.mark.django_db
class TestIndexAPIView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_index_list_works(self) -> None:
        mixer.blend(Author)
        mixer.blend(Author)
        mixer.blend(BookInstance)
        mixer.blend(BookInstance)

        url = reverse('catalog:index')

        response = self.client.get(url)

        assert response.json != None
        assert len(response.data) == 4
        assert response.data['num_books'] == 2
        assert response.data['num_instance'] == 2
        assert response.data['num_instance_available'] == 1
        assert response.data['num_author'] == 2
        assert response.status_code == 200


@pytest.mark.django_db
class TestBookListView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_book_list_works(self) -> None:
        mixer.blend(Book)
        mixer.blend(Book)
        mixer.blend(Book)
        mixer.blend(Book)

        url = reverse('catalog:books')

        response = self.client.get(url)

        assert response.json != None
        assert len(response.data['book_list']) == 4
        assert len(response.data['book_list'][0]) == 3
        assert response.status_code == 200


@pytest.mark.django_db
class TestBookDetailView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        print(self.client, "self.client")

    def test_book_detail_list_works(self) -> None:
        author = mixer.blend(Author)
        book = mixer.blend(Book, author=author)
        mixer.blend(BookInstance, book=book)

        url = reverse('catalog:book-detail', kwargs={"id": book.id})

        response = self.client.get(url)

        assert response.json != None
        assert len(response.data['book']) == 5
        assert len(response.data['authors'][0]) == 2
        assert len(response.data['book_instance_set'][0]) == 3
        assert len(response.data) == 3
        assert response.status_code == 200


@pytest.mark.django_db
class TestAuthorListView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_author_list_works(self) -> None:
        mixer.blend(Author)
        mixer.blend(Author)
        mixer.blend(Author)
        mixer.blend(Author)

        url = reverse('catalog:authors')

        response = self.client.get(url)

        assert response.json != None
        assert len(response.data['author_list']) == 4
        assert len(response.data['author_list'][0]) == 4
        assert response.status_code == 200
