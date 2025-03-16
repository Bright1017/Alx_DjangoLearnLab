from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')

    def __str__(self):
        return self.title
    
    
# Step 1: Install Django and Django REST Framework
# Run the following commands in your terminal
# pip install django djangorestframework

# Step 2: Create Django project and app
# django-admin startproject advanced_api_project
# cd advanced_api_project
# python manage.py startapp api

# Step 3: Configure settings.py
# Step 4: Define models in api/models.py
# Step 5: Run migrations
# python manage.py makemigrations api
# python manage.py migrate

# Step 6: Create serializers in api/serializers.py
# Step 7: Document the setup in models.py and serializers.py
# Comments have been added within the code to explain each section

# Step 8: Testing
# Use Django shell to test manually
# python manage.py shell
# from api.models import Author, Book
# from api.serializers import AuthorSerializer, BookSerializer
# author = Author.objects.create(name="J.K. Rowling")
# book = Book.objects.create(title="Harry Potter", publication_year=1997, author=author)
# serializer = AuthorSerializer(author)
# print(serializer.data)