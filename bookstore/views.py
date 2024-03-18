from django.db.models import Q
from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination

from .models import Book
from .serializers import BookSerializer


class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 1000


class BookList(generics.ListAPIView):
    queryset = Book.objects.all().order_by("-downloads")
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author", "language", "subjects", "bookshelves"]
    pagination_class = CustomPagination


# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all().order_by("-downloads")
#     serializer_class = BookSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         # Get query parameters
#         query_params = self.request.GET

#         if gutenberg_ids := query_params.getlist("gutenberg_id"):
#             queryset = queryset.filter(gutenberg_id__in=gutenberg_ids)

#         if languages := query_params.getlist("language"):
#             queryset = queryset.filter(language__in=languages)

#         if topics := query_params.getlist("topic"):
#             topic_filter = Q()
#             for topic in topics:
#                 topic_filter |= Q(subjects__icontains=topic) | Q(
#                     bookshelves__icontains=topic
#                 )
#             queryset = queryset.filter(topic_filter)

#         if authors := query_params.getlist("author"):
#             queryset = queryset.filter(author__icontains=authors)

#         if titles := query_params.getlist("title"):
#             queryset = queryset.filter(title__icontains=titles)

#         return queryset


# In case the number of books that meet the criteria exceeds 20, the API should
# return only 20 books at a time and support the means of retrieving the next sets
# of 20 books till all books are retrieved.  - PAGINATION
