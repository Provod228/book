from django.urls import path, include
from .views import BookDetailView, BookListView, AuthorListView

app_name = 'catalog'

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:id>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]