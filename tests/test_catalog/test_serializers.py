from catalog.serializers import *
from catalog.models import *
import pytest


@pytest.mark.parametrize(
    "serializer, test_data",
    [
        [IndexSerializer, "test_count_data"],
        [BookListSerializer, "test_book_data"],
        [BookDetailSerializer, "test_book_data"],
        [BookAuthorDetailSerializer, "test_author_data"],
        [AuthorListSerializer, "test_author_data"],
        [BookInstanceDetailSerializer, "test_book_instance_data"],
    ],
)
def test_all_serializer(serializer, test_data, request) -> None:
    test_data = request.getfixturevalue(test_data)
    serial = serializer(data=test_data)
    assert serial.is_valid()
