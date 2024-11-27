import factory
from .models import Book, Genre, Language, Author, Status, BookInstance
from datetime import UTC


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker("name")


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language

    name = factory.Faker("name")


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    data_of_birth = factory.Faker("date_time", tzinfo=UTC)
    data_of_death = factory.Faker("date_time", tzinfo=UTC)


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status

    name = factory.Faker("name")


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    title = factory.Faker("sentence")
    genre = factory.SubFactory(GenreFactory)
    language = factory.SubFactory(LanguageFactory)
    summary = factory.Faker("paragraph")
    isbn = factory.Faker("isbn")

    @factory.post_generation
    def author(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.author.add(*extracted)


class BookInstanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BookInstance

    book = factory.SubFactory(BookFactory)
    inv_nom = factory.Faker("inv_nom")
    imprint = factory.Faker("imprint")
    status = factory.SubFactory(StatusFactory)
    due_back = factory.Faker("date_time", tzinfo=UTC)

