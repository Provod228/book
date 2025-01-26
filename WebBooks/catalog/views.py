from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import login
from .forms import SignUpForm, AuthorForm, BookForm
from django.urls import reverse

# Create your views here.


class UserRegistrationView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request):
        form = SignUpForm()
        return Response({'form': form})

    def post(self, request) -> Response:
        form = SignUpForm(request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('catalog:index'))
        else:
            return Response({'form': form})


class AuthorAddView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'author_add.html'

    def get(self, request):
        form = AuthorForm()
        return Response({'form': form})

    def post(self, request) -> Response:
        form = AuthorForm(request.data)
        if form.is_valid():
            form.save()
            return redirect(reverse('catalog:index'))
        else:
            return Response({'form': form})


class BookAddView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_add.html'

    def get(self, request):
        form = BookForm()
        return Response({'form': form})

    def post(self, request) -> Response:
        form = BookForm(request.data)
        if form.is_valid():
            form.save()
            return redirect(reverse('catalog:index'))
        else:
            return Response({'form': form})


class MainPageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_page.html'

    def get(self, request: None) -> Response:
        return Response()


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request: None) -> Response:
        num_books = Book.objects.count()
        num_instance = BookInstance.objects.count()
        num_instance_available = BookInstance.objects.filter(status__exact=2).count()
        num_author = Author.objects.count()
        counts_models = {
            'num_books': num_books,
            'num_instance': num_instance,
            'num_instance_available': num_instance_available,
            'num_author': num_author,
        }
        serializer = IndexSerializer(data=counts_models)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class BookListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_list.html'

    def get(self, request: None) -> Response:
        book_list = Book.objects.all()
        return Response({'book_list': BookListSerializer(book_list, many=True).data})


class BookDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_detail.html'

    def get(self, request: None, id: int) -> Response:
        book = Book.objects.get(pk=id)
        author = book.author.all()
        book_instance_set = book.bookinstance_set.all()
        return Response({
            'book': BookDetailSerializer(book).data,
            'authors': BookAuthorDetailSerializer(author, many=True).data,
            'book_instance_set': BookInstanceDetailSerializer(book_instance_set, many=True).data,
                         })


class AuthorListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'author_list.html'

    def get(self, request: None) -> Response:
        author_list = Author.objects.all()
        return Response({'author_list': AuthorListSerializer(author_list, many=True).data})
