from catalog.serializers import *
from catalog.models import *


def test_index_serializers(test_count_data: dict) -> None:
    serializer = IndexSerializer(data=test_count_data)
    assert serializer.is_valid()


def test_book_list_serializers(test_book_data: dict) -> None:
    serializer = BookListSerializer(data=test_book_data)
    assert serializer.is_valid()


def test_book_detail_serializers(test_book_data: dict) -> None:
    serializer = BookDetailSerializer(data=test_book_data)
    assert serializer.is_valid()


def test_book_author_detail_serializers(test_author_data: dict) -> None:
    serializer = BookAuthorDetailSerializer(data=test_author_data)
    assert serializer.is_valid()


def test_author_list_serializers(test_author_data: dict) -> None:
    serializer = AuthorListSerializer(data=test_author_data)
    assert serializer.is_valid()


def test_book_instance_detail_serializers(test_book_instance_data: dict) -> None:
    serializer = BookInstanceDetailSerializer(data=test_book_instance_data)
    assert serializer.is_valid()
