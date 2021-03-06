from django.urls import path
from . import views


urlpatterns = [
    path(
        "api/allpackages/<int:pk>/booking",
        views.BookingCreateAPIView.as_view(),
        name="api-booking",
    ),
    path("api/mybooking", views.BookingListAPIView.as_view(), name="api-mybooking"),
    path(
        "api/custombooking",
        views.CustomBookingCreateAPIView.as_view(),
        name="api-custombooking",
    ),
    path(
        "api/mycustombooking",
        views.CustomBookingListAPIView.as_view(),
        name="api-mycustombooking",
    ),
]
