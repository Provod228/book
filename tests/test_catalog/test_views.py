import pytest
from catalog.models import Book, BookInstance, Author
from catalog.urls import *
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.test import TestCase


@pytest.mark.django_db
class TestIndexAPIView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_index_list_works(self) -> None:
        mixer.blend(Author)
        mixer.blend(Author)
        mixer.blend(BookInstance)
        mixer.blend(BookInstance)

        response = self.client.get(reverse('catalog:index'))

        assert response.json != None
        assert len(response.data) == 4
        assert response.data['num_books'] == 2
        assert response.data['num_instance'] == 2
        assert response.data['num_instance_available'] == 1
        assert response.data['num_author'] == 2
        assert response.status_code == 200


@pytest.mark.django_db
class TestBookListView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_book_list_works(self) -> None:
        mixer.blend(Book)
        mixer.blend(Book)
        mixer.blend(Book)
        mixer.blend(Book)

        response = self.client.get(reverse('catalog:books'))

        assert response.json != None
        assert len(response.data['book_list']) == 4
        assert len(response.data['book_list'][0]) == 3
        assert response.status_code == 200


@pytest.mark.django_db
class TestBookDetailView(TestCase):
    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_book_detail_list_works(self) -> None:
        mixer.blend(Book)
        # mixer.blend(Book)
        # mixer.blend(Book)
        # mixer.blend(Book)

        print(Book.objects.all().values_list()[0][0])

        response = self.client.get(reverse('catalog:book-detail'))

        # Потом сделаю нормальные assert
        # assert response.json != None
        # assert len(response.data['book_list']) == 4
        # assert len(response.data['book_list'][0]) == 3
        # assert response.status_code == 200


@pytest.mark.django_db
class TestAuthorListView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_author_list_works(self) -> None:
        mixer.blend(Author)
        mixer.blend(Author)
        mixer.blend(Author)
        mixer.blend(Author)

        response = self.client.get(reverse('catalog:authors'))

        assert response.json != None
        assert len(response.data['author_list']) == 4
        assert len(response.data['author_list'][0]) == 4
        assert response.status_code == 200