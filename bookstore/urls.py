from django.urls import path

from .views import *

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
]
