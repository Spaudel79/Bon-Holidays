from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class BlogPostPageNumberPagination(PageNumberPagination):
    page_size = 3

class CommentPageNumberPagination(PageNumberPagination):
    page_size = 2