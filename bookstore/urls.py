from django.urls import path

from .views import BookDetail, BookListView

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:book_id>/", BookDetail.as_view(), name="book-detail"),
]
