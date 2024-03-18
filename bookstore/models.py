from django.db import models


class Book(models.Model):
    gutenberg_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    subjects = models.TextField()
    bookshelves = models.TextField()
    downloads = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-downloads"]

    def __str__(self):
        return str(self.title)

    # A list of book objects, each of which contains the following:
    #       Title of the book
    #       Information about the author
    #       Genre
    #       Language
    #       Subject(s)
    #       Bookshelf(s)
