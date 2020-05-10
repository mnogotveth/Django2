from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

# Create your views here.
from django.views import View
from .models import Book
from .serializers import BookSerializer


def first(request):
    books = Book.objects.all()
    return render(request, 'test.html', {
        'books': books
    })

class Second(View):
    def get(self, request):
        return HttpResponse(self.output)

class BookViewSet(viewsets.ModelViewSet):
        serializer_class = BookSerializer
        queryset = Book.objects.all()
        authentication_classes = (TokenAuthentication,)

    # books = Book.objects.all()
    # books = Book.objects.filter(is_published = True)
    #book = Book.objects.get(id = 1)

    #output = ''

    # for book in books:
    #     output += (f'We have {book.title} with ID {book.id} in our Database<br>')

    #output = (f'We have {book.title} with ID {book.id} in our Database<br>')
