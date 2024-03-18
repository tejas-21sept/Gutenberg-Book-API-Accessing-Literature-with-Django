from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


class BookListView(APIView):
    def get(self, request):
        language = request.GET.get("language", None)
        mime_type = request.GET.get("mime_type", None)
        topic = request.GET.get("topic", None)
        author = request.GET.get("author", None)
        title = request.GET.get("title", None)

        print(
            f"\nlanguage - {language}\nmime_type - {mime_type}\ntopic - {topic}\nauthor - {author}\ntitle - {title}\n"
        )

        # Split multiple values by comma and create list
        languages = language.split(",") if language else None
        topics = topic.split(",") if topic else None
        author = author.split(",") if author else None
        title = title.split(",") if title else None
        mime_type = mime_type.split(",") if mime_type else None

        # Filter based on query parameters
        books = Book.objects.all()
        if languages:
            books = books.filter(language__in=languages)
        if mime_type:
            books = books.filter(mime_type__iexact=mime_type)
        if topics:
            # Use Q objects for OR condition in query
            topic_query = Q()
            for t in topics:
                topic_query |= Q(subject__icontains=t) | Q(bookshelf__icontains=t)
            books = books.filter(topic_query)
        if author:
            books = books.filter(author__icontains=author)
        if title:
            books = books.filter(title__icontains=title)

        # Ordering by popularity (number of download_count)
        books = books.order_by("-download_count")

        # Pagination
        paginator = Paginator(books, 20)
        page = request.GET.get("page")
        try:
            book_page = paginator.page(page)
        except PageNotAnInteger:
            book_page = paginator.page(1)
        except EmptyPage:
            book_page = paginator.page(paginator.num_pages)

        serializer = BookSerializer(book_page, many=True)
        data = {"count": paginator.count, "books": serializer.data}
        return Response(data)


class BookDetail(APIView):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
