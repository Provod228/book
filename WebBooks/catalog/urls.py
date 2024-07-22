from django.urls import path, include
from .views import BookDetailView, BookListView, AuthorListView, index

app_name = 'catalog'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:id>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('accounts/', include('django.contrib.auth.urls'))
]
