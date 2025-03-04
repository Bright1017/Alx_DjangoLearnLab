from django.urls import path
from . import views

urlpattern = [
    path("bookshelf", view=book_list)
]
