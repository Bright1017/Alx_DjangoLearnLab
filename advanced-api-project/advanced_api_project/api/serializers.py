from .models import Author, Book
from rest_framework.serializers import ModelSerializer, ValidationError
import datetime

class Bookserializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(ModelSerializer):
    books = Bookserializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']




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