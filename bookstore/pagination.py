from rest_framework.pagination import LimitOffsetPagination


class BookPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 20
