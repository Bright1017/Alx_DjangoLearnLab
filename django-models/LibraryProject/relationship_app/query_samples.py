import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

if __name__ == "__main__":
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    print(f"Books by {author_name}: {[book.title for book in get_books_by_author(author_name)]}")
    print(f"Books in {library_name}: {[book.title for book in get_books_in_library(library_name)]}")
    print(f"Librarian for {library_name}: {get_librarian_for_library(library_name).name}")
