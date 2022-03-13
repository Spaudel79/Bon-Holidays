from django.urls import include, path

from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path("api/tags", views.TagsAPIView.as_view(), name="api-tags"),
    path(
        "api/blog-post", views.BlogPostListFrontAPIView.as_view(), name="api-blog-post"
    ),
    path(
        "api/blog-post/all",
        views.BlogPostAllListAPIView.as_view(),
        name="api-blog-post",
    ),
    path(
        "api/blog-post/<int:pk>",
        views.BlogPostDetailsListAPIView.as_view(),
        name="api-blog-post_details",
    ),
    path(
        "api/comments/<int:blog>",
        views.CommentListAPIView.as_view(),
        name="api-comments",
    ),
    path(
        "api/blog-post/<int:pk>/postcomment",
        views.CommentCreateAPIView.as_view(),
        name="api-postcomment",
    ),
    path("api/subscriber", views.SubscribersView.as_view(), name="api-subsciber"),
]
