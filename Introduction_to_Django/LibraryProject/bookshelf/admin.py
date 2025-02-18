from django.contrib import admin
from .models import Book

# Register your models here.
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)