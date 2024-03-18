from django.contrib import admin

from .models import (
    Author,
    Book,
    BookAuthors,
    BookBookshelves,
    BookLanguages,
    Bookshelf,
    BookSubjects,
    Format,
    Language,
    Subject,
)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthors)
admin.site.register(BookBookshelves)
admin.site.register(BookLanguages)
admin.site.register(BookSubjects)
admin.site.register(Bookshelf)
admin.site.register(Format)
admin.site.register(Language)
admin.site.register(Subject)
