from catalog.serializers import *
from catalog.models import *


def test_index_serializers(test_count_data):
    serializer = IndexSerializer(data=test_count_data)
    assert serializer.is_valid()


def test_book_list_serializers(test_book_data):
    serializer = BookListSerializers(data=test_book_data)
    assert serializer.is_valid()


def test_book_detail_serializers(test_book_data):
    serializer = BookDetailSerializers(data=test_book_data)
    assert serializer.is_valid()


def test_book_author_detail_serializers(test_author_data):
    serializer = BookAuthorDetailSerializers(data=test_author_data)
    assert serializer.is_valid()


def test_author_list_serializers(test_author_data):
    serializer = AuthorListSerializers(data=test_author_data)
    assert serializer.is_valid()


def test_book_instance_detail_serializers(test_book_instance_data):
    serializer = BookInstanceDetailSerializers(data=test_book_instance_data)
    assert serializer.is_valid()


