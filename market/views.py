from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Book
import json
from django.http import JsonResponse


def market(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def search_books(request):
    query = request.GET.get('query')
    if query:
        results = Book.objects.filter(name__icontains=query) | Book.objects.filter(author_name__icontains=query)
    else:
        results = Book.objects.all()
    return render(request, 'search_results.html', {'results': results})


def book_list(request):
    # Retrieve book data from JSON or any other source
    with open('books.json') as f:
        books = json.load(f)
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, book_id):
    # Retrieve book data from JSON or any other source
    with open('books.json') as f:
        books = json.load(f)
    book = next((book for book in books if book['id'] == book_id), None)
    return render(request, 'book_detail.html', {'book': book})


def book_json(request):
    books_data = [
        {
            "name": "The Great Gatsby",
            "page_count": 180,
            "category": "Fiction",
            "author_name": "F. Scott Fitzgerald",
            "price": 12.99
        },
        {
            "name": "To Kill a Mockingbird",
            "page_count": 281,
            "category": "Fiction",
            "author_name": "Harper Lee",
            "price": 10.50
        },
        {
            "name": "1984",
            "page_count": 328,
            "category": "Dystopian",
            "author_name": "George Orwell",
            "price": 9.99
        }
    ]
    return JsonResponse(books_data, safe=False)