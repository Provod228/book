from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact=2).count()
    num_author = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instance': num_instance,
                           'num_instance_available': num_instance_available,
                           'num_author': num_author,
                           'num_visits': num_visits,
                           }
                  )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    template_name = 'book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    paginate_by = 3


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
    template_name = 'author_list.html'
