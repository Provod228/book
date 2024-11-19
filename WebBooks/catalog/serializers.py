from rest_framework import serializers
from .models import *


class IndexSerializer(serializers.Serializer):
    num_books = serializers.IntegerField()
    num_instance = serializers.IntegerField()
    num_instance_available = serializers.IntegerField()
    num_author = serializers.IntegerField()


class BookDetailSerializer(serializers.ModelSerializer):
    genre = serializers.CharField()
    language = serializers.CharField()

    class Meta:
        model = Book
        fields = ['title', 'genre', 'summary', 'isbn', 'language']


class BookAuthorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookInstanceDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField()

    class Meta:
        model = BookInstance
        fields = ['status', 'id', 'imprint']


class BookListSerializer(serializers.ModelSerializer):
    genre = serializers.CharField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'genre']


class AuthorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'data_of_birth', 'data_of_death']
