from catalog.serializers import *
from catalog.models import *


def test_index_serializer(test_count_data: dict) -> None:
    serializer = IndexSerializer(data=test_count_data)
    assert serializer.is_valid()


def test_book_list_serializer(test_book_data: dict) -> None:
    serializer = BookListSerializer(data=test_book_data)
    assert serializer.is_valid()


def test_book_detail_serializer(test_book_data: dict) -> None:
    serializer = BookDetailSerializer(data=test_book_data)
    assert serializer.is_valid()


def test_book_author_detail_serializer(test_author_data: dict) -> None:
    serializer = BookAuthorDetailSerializer(data=test_author_data)
    assert serializer.is_valid()


def test_author_list_serializer(test_author_data: dict) -> None:
    serializer = AuthorListSerializer(data=test_author_data)
    assert serializer.is_valid()


def test_book_instance_detail_serializer(test_book_instance_data: dict) -> None:
    serializer = BookInstanceDetailSerializer(data=test_book_instance_data)
    assert serializer.is_valid()


# @pytest.mark.parametrize("endpoint", [
#     [IndexSerializer, test_count_data],
#     [BookListSerializer, test_book_data],
#     [BookDetailSerializer, test_book_data],
#     [BookAuthorDetailSerializer, test_author_data],
#     [AuthorListSerializer, test_author_data],
#     [BookInstanceDetailSerializer, test_book_instance_data],
# ])
