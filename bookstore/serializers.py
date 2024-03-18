from rest_framework import serializers

from .models import *


class SubjectSerializer(serializers.ModelSerializer):
    """Serializer for the Subject model."""

    class Meta:
        model = Subject
        fields = ("name",)


class BookshelfSerializer(serializers.ModelSerializer):
    """Serializer for the Bookshelf model."""

    class Meta:
        model = Bookshelf
        fields = ("name",)


class FormatSerializer(serializers.ModelSerializer):
    """Serializer for the Format model."""

    class Meta:
        model = Format
        fields = ("mime_type", "url")


class LanguageSerializer(serializers.ModelSerializer):
    """Serializer for the Language model."""

    class Meta:
        model = Language
        fields = ("id", "code")


class BookLanguagesSerializer(serializers.ModelSerializer):
    """Serializer for the BookLanguages model."""

    language = LanguageSerializer()

    class Meta:
        model = BookLanguages
        fields = ("language",)


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model."""

    class Meta:
        model = Author
        fields = ("id", "name", "birth_year", "death_year")


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model."""

    languages = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    topics = serializers.SerializerMethodField()
    format = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "media_type",
            "authors",
            "languages",
            "topics",
            "format",
        )

    def get_languages(self, obj):
        """Get languages associated with the book."""
        book_languages = BookLanguages.objects.filter(book=obj)
        return BookLanguagesSerializer(book_languages, many=True).data

    def get_authors(self, obj):
        """Get authors associated with the book."""
        book_authors = BookAuthors.objects.filter(book=obj)
        authors = [author.author for author in book_authors]
        return AuthorSerializer(authors, many=True).data

    def get_topics(self, obj):
        """Get topics (subjects and bookshelves) associated with the book."""
        book_subjects = BookSubjects.objects.filter(book=obj)
        book_bookshelves = BookBookshelves.objects.filter(book=obj)

        subjects = [book_subject.subject for book_subject in book_subjects]
        shelves = [book_bookshelf.bookshelf for book_bookshelf in book_bookshelves]

        subject_serializer = SubjectSerializer(subjects, many=True)
        shelf_serializer = BookshelfSerializer(shelves, many=True)

        return {
            "subjects": subject_serializer.data,
            "bookshelves": shelf_serializer.data,
        }

    def get_format(self, obj):
        """Get formats associated with the book."""
        formats = Format.objects.filter(book=obj)
        format_serializer = FormatSerializer(formats, many=True)
        return format_serializer.data
