# This is an auto-generated Django model module.

from django.db import models

class Author(models.Model):
    """Model representing an author."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = "books_author"

    def __str__(self):
        return self.name


class Language(models.Model):
    """Model representing a language."""
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=4)

    class Meta:
        db_table = "books_language"

    def __str__(self):
        return self.code


class Subject(models.Model):
    """Model representing a subject."""
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        db_table = "books_subject"

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book."""
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)

    class Meta:
        db_table = "books_book"

    def __str__(self):
        return self.title


class Bookshelf(models.Model):
    """Model representing a bookshelf."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "books_bookshelf"

    def __str__(self):
        return self.name


class Format(models.Model):
    """Model representing a format of a book."""
    id = models.AutoField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_format"

    def __str__(self):
        return f"{self.mime_type} - {self.url}"


class BookAuthors(models.Model):
    """Model representing a book and its author."""
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_authors"

    def __str__(self):
        return f"{self.book.title} - {self.author.name}"


class BookBookshelves(models.Model):
    """Model representing a book and its bookshelf."""
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_bookshelves"

    def __str__(self):
        return f"{self.book.title} - {self.bookshelf.name}"


class BookLanguages(models.Model):
    """Model representing a book and its language."""
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_languages"

    def __str__(self):
        return f"{self.book.title} - {self.language.code}"


class BookSubjects(models.Model):
    """Model representing a book and its subject."""
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_subjects"

    def __str__(self):
        return f"{self.book.title} - {self.subject.name}"

