# books/tests/test_views.py
from django.test import RequestFactory, TestCase

from bookstore.models import Book
from bookstore.views import BookList


class BookListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = BookList.as_view()
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre="Test Genre",
            language="Test Language",
            subjects="Test Subject",
            bookshelves="Test Bookshelf",
            downloads=0,
        )

    def test_book_list_view(self):
        request = self.factory.get("/books/")
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.book.title.encode(), response.content)
