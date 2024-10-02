from rest_framework import serializers
from .models import Book, Author


# class IndexSerializers(serializers.Serializer):
#     counts_db = serializers.()


class BookListSerializers(serializers.Serializer):
    title = serializers.CharField()
    genre = serializers.CharField()
    id = serializers.IntegerField()


class AuthorListSerializers(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    data_of_birth = serializers.DateField()
    data_of_death = serializers.DateField()

