from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from django.contrib.auth import get_user_model    # использовать при создании своего User сущности
#
# User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
