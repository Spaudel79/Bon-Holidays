from django.urls import include, path
from rest_framework import routers
# from .views import BlogPostViewSet, CommentViewSet
from django.urls import path, re_path, include
from .import views


urlpatterns = [

        path('api/booking', views.BookingCreateAPIView.as_view(), name='api-booking'),
]