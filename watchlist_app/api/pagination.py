from rest_framework.pagination import PageNumberPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "p"
