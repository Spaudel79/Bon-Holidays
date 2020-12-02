from django.urls import include, path
from rest_framework import routers
# from .views import BlogPostViewSet, CommentViewSet
from django.urls import path, re_path, include
from .import views


urlpatterns = [

        path('api/allpackages/<int:pk>/booking', views.BookingCreateAPIView.as_view(), name='api-booking'),

        path('api/mybooking', views.BookingListAPIView.as_view(), name='api-mybooking'),
        path('api/custombooking', views.CustomBookingCreateAPIView.as_view(), name='api-custombooking'),
]