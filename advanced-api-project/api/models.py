from django.db import models

# Create your models here.

class Author(models.Model):
    """Represents an author with a name. Each author can have multiple books."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Represents a book with title, publication year, and a foreign key to Author."""
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title