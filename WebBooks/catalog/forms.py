from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from catalog.models import Author, Book
# from django.contrib.auth import get_user_model    # использовать при создании своего User сущности
#
# User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'data_of_birth', 'data_of_death')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'genre', 'language', 'author', 'summary', 'isbn')

