from django.test import TestCase

from bookstore.models import Book


class BookModelTestCase(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre="Test Genre",
            language="Test Language",
            subjects="Test Subject",
            bookshelves="Test Bookshelf",
            downloads=0,
        )
        self.assertEqual(book.title, "Test Book")
