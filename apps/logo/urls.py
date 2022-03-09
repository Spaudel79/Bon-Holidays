from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path("api/logo", views.LogoAPIView.as_view(), name="api-logo"),
]
