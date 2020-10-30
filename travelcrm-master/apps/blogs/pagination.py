from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class BlogPostPageNumberPagination(PageNumberPagination):
    page_size = 4

class CommentPageNumberPagination(PageNumberPagination):
    page_size = 2