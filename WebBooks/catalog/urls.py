from django.urls import path, include
from .views import *

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/add', BookAddView.as_view(), name='book_add'),
    path('books/<int:id>', BookDetailView.as_view(), name='book-detail'),
    path('authors/add', AuthorAddView.as_view(), name='author_add'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('accounts/signup', UserRegistrationView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
