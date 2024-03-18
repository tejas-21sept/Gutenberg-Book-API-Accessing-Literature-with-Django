from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response

from .models import Book
from .pagination import BookPagination
from .serializers import BookSerializer


class BookListAPIView(generics.ListAPIView):
    """
    API endpoint for listing books with filtering and pagination support.
    """

    serializer_class = BookSerializer
    pagination_class = BookPagination

    def get_queryset(self):
        """
        Retrieves the queryset of books based on provided filter parameters.

        Returns:
            queryset: A queryset of Book objects filtered based on query parameters.
        """
        queryset = Book.objects.all().order_by("id")

        # Filtering based on query parameters
        book_ids = self.request.GET.getlist("book_id")
        languages = self.request.GET.getlist("language")
        mime_types = self.request.GET.getlist("mime_type")
        topics = self.request.GET.getlist("topic")
        authors = self.request.GET.getlist("author")
        titles = self.request.GET.getlist("title")

        # Filtering by book IDs
        if book_ids:
            queryset = queryset.filter(gutenberg_id__in=book_ids)

        # Filtering by languages
        if languages:
            queryset = queryset.filter(booklanguages__language__code__in=languages)

        # Filtering by MIME types
        if mime_types:
            queryset = queryset.filter(format__mime_type__in=mime_types)

        # Filtering by topics (subjects or bookshelves)
        if topics:
            queryset = queryset.filter(
                Q(booksubjects__subject__name__icontains=topics)
                | Q(bookbookshelves__bookshelf__name__icontains=topics)
            )

        # Filtering by authors
        if authors:
            queryset = queryset.filter(bookauthors__author__name__icontains=authors)

        # Filtering by titles
        if titles:
            queryset = queryset.filter(title__icontains=titles)

        return queryset
