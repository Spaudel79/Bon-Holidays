from django.urls import include, path

from . import views


urlpatterns = [
    path(
        "api/destinations",
        views.DestinationFrontListAPIView.as_view(),
        name="api-destinations",
    ),
    path(
        "api/destinations/<int:pk>",
        views.DestinationPackageListAPIView.as_view(),
        name="api-destinations-packages",
    ),
    path("api/allpackages", views.AllPackageAPIView.as_view(), name="api-allpackages"),
    path("api/packages", views.PackageAPIView.as_view(), name="api-packages"),
    path(
        "api/allpackagescount",
        views.PackageCountView.as_view(),
        name="api-allpackagescount",
    ),
    path(
        "api/allpackages/<int:pk>",
        views.AllPackageDetailAPIView.as_view(),
        name="api-package-detail",
    ),
    path(
        "api/allpackages/<int:pk>/postreview",
        views.ReviewAPIView.as_view(),
        name="api-review-post",
    ),
    path(
        "api/newactivities",
        views.NewActivityListAPIView.as_view(),
        name="api-newactivities",
    ),
]
