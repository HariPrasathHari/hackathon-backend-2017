from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class PostLimitOffset(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

class PostPageNumberPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 10
