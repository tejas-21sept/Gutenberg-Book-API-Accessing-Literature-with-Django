from django.urls import path

from .views import BookList

urlpatterns = [
    path("booklist/", BookList.as_view(), name="book-list"),
]
