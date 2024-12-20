# books/views.py
from django.shortcuts import render
from .models import Book

def books_list(request):
    books = {
    'books' : Book.objects.all()
    }
    return render(request, 'books_list.html', books)
