from django.db import models


class Author(models.Model):
    birth_year = models.SmallIntegerField(null=True)
    death_year = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=128)


class Book(models.Model):
    download_count = models.IntegerField(null=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField(null=True)


class BookAuthors(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookBookshelves(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookshelf_id = models.IntegerField()


class BookLanguages(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language_id = models.IntegerField()


class BookSubjects(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    subject_id = models.IntegerField()


class Bookshelf(models.Model):
    name = models.CharField(max_length=64)


class Format(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Language(models.Model):
    code = models.CharField(max_length=4)


class Subject(models.Model):
    name = models.TextField()
