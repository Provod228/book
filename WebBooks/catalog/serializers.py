from rest_framework import serializers


class IndexSerializer(serializers.Serializer):
    num_books = serializers.IntegerField()
    num_instance = serializers.IntegerField()
    num_instance_available = serializers.IntegerField()
    num_author = serializers.IntegerField()


class BookDetailSerializers(serializers.Serializer):
    title = serializers.CharField()
    genre = serializers.CharField()
    summary = serializers.CharField()
    isbn = serializers.CharField()
    language = serializers.CharField()


class BookAuthorDetailSerializers(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class BookInstanceDetailSerializers(serializers.Serializer):
    status_display = serializers.DjangoModelField()
    imprint = serializers.CharField()
    id = serializers.IntegerField()
    status = serializers.CharField()


class BookListSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.CharField()


class AuthorListSerializers(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    data_of_birth = serializers.DateField()
    data_of_death = serializers.DateField()

