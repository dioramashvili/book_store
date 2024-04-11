from . import views
from django.urls import path
from .views import search_books
from .views import book_json


urlpatterns = [
    path('market/', views.market, name='market'),
    path('search/', search_books, name='search_books'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/json/', book_json, name='book_json'),
]

