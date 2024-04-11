from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # URL for book listing
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # URL for book detail
]
