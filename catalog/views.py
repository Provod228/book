from .models import Book, Author, BookInstance
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        num_books = Book.objects.all().count()
        num_instance = BookInstance.objects.all().count()
        num_instance_available = BookInstance.objects.filter(status__exact=2).count()
        num_author = Author.objects.count()
        return Response({
                        'num_books': num_books,
                        'num_instance': num_instance,
                        'num_instance_available': num_instance_available,
                        'num_author': num_author,
                        })


class BookListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_list.html'

    def get(self, request):
        book_list = Book.objects.all()
        return Response({'book_list': book_list})


class BookDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_detail.html'

    def get(self, request, id):
        book = Book.objects.get(pk=id)
        return Response({'book': book})


class AuthorListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'author_list.html'

    def get(self, request):
        author_list = Author.objects.all()
        return Response({'author_list': author_list})