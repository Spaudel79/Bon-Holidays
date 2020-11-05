from django.urls import include, path
from rest_framework import routers
from . import views
from django.urls import path, re_path, include
from .import views

# router = routers.DefaultRouter()
# router.register(r'partner-application', views.PartnerApplicationViewSet)
# router.register(r'bookmundi-account', views.BookmundiAccountViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
        # path('', views.Homepage.as_view(), name='home'),
        path('api/register', views.RegisterUserView.as_view(), name='api-register'),
        path('api/login', views.LoginUserView.as_view(), name='api-login'),
        path('api/logout', views.Logout.as_view(), name='api-logout'),
        # path('blog-post/<int:pk>', views.BlogPostDetailsListAPIView.as_view(), name='api-blog-post_details'),
        # path('comments/', views.CommentCreateAPIView.as_view(), name='api-comments'),


]