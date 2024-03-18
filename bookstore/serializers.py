from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "genre",
            "language",
            "subject",
            "bookshelf",
            "download_links",
            "download_count",
        ]
