from django.test import TestCase

from bookstore.models import Book
from bookstore.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_book_serializer(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre="Test Genre",
            language="Test Language",
            subjects="Test Subject",
            bookshelves="Test Bookshelf",
            downloads=0,
        )
        serializer = BookSerializer(book)
        expected_data = {
            "title": "Test Book",
            "author": "Test Author",
        }
        self.assertEqual(serializer.data, expected_data)
