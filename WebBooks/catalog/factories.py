import random
import factory
from .models import Book, Genre, Language, Author, Status, BookInstance


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
    data_of_birth = factory.Faker("date_time")
    data_of_death = factory.Faker("date_time")


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
    isbn = str(random.randint(1000000000000, 9999999999999))
    #  author = [AuthorFactory.create() for _ in range(random.randint(1, 5))]

    @factory.post_generation
    def author(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.author.add(*extracted)


class BookInstanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BookInstance

    book = factory.SubFactory(BookFactory)
    inv_nom = factory.Faker('random_int', min=0, max=100)
    imprint = factory.Faker("company")
    status = factory.SubFactory(StatusFactory)
    due_back = factory.Faker("date_time")
