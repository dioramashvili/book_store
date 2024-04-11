from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = Book.DisplayFields
    search_fields = ('name', 'author_name')
    list_per_page = 3
