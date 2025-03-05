"""
2. Utilizing the Django Admin Interface
mandatory
Score: 0.0% (Checks completed: 0.0%)
Objective: Gain practical experience with the Django admin interface by configuring the admin to manage the Book model. This task will demonstrate how to use Django’s built-in admin interface to perform data management tasks efficiently.

Task Description:
Enhance your bookshelf app by integrating the Book model with the Django admin interface. Customize the admin display to improve the management and visibility of book data, and document the process to ensure consistent setup and configuration.

Steps:
Register the Book Model with the Django Admin:

Modify bookshelf/admin.py to include the Book model, enabling admin functionalities for it.
Customize the Admin Interface:

Implement custom configurations to display title, author, and publication_year in the admin list view.
Configure list filters and search capabilities to enhance the admin’s usability for Book entries.
"""

from django.contrib import admin
from .models import CustomUser, Book

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo')

class BookAdmin(admin.ModelAdmin):
    list_filter = (("title", "author"))
    search_fields = ("title", "author")

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)