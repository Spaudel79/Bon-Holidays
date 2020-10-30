from django.urls import include, path
from rest_framework import routers
# from .views import BlogPostViewSet, CommentViewSet
from django.urls import path, re_path, include
from .import views

# router = routers.DefaultRouter()
# router.register(r'blog-post', BlogPostViewSet)
# router.register(r'comments', CommentViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]



urlpatterns = [

        path('api/blog-post', views.BlogPostListFrontAPIView.as_view(), name='api-blog-post'),
        path('api/blog-post/all', views.BlogPostAllListAPIView.as_view(), name='api-blog-post'),
        path('api/blog-post/<int:pk>', views.BlogPostDetailsListAPIView.as_view(), name='api-blog-post_details'),
        path('api/comments/<int:blog>', views.CommentListAPIView.as_view(), name='api-comments'),
        # path('api/user/<int:pk>/blog-post/<int:pk>/postcomment', views.CommentCreateAPIView.as_view(), name='api-postcomment'),


]



