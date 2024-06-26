from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class watchlistpagination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    # last_page_strings = 'end'

class watchlistlimitoffset(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10

class Cursorpage(CursorPagination):
    page_size = 5