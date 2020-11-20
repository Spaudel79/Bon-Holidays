# packages/urls.py
from django.urls import include, path
from rest_framework import routers
# from .views import PackageViewSet, DestinationViewSet, TopActtractionsViewset, TopActivitiesViewset
from .import views

# router = routers.DefaultRouter()
# router.register(r'packages', PackageViewSet)
# router.register(r'destination', DestinationViewSet)
# router.register(r'top-attractions', TopActtractionsViewset)
# router.register(r'top-activities', TopActivitiesViewset)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [

        # path('api/destinations', views.DestinationFrontListAPIView.as_view(), name='api-destinations'),
        # path('api/traveldeals', views.DestinationFrontListAPIView.as_view(), name='api-traveldeals'),

        path('api/destinations', views.DestinationFrontListAPIView.as_view(), name='api-destinations'),
        path('api/destinations/<int:pk>', views.DestinationPackageListAPIView.as_view(), name='api-destinations-packages'),
        path('api/allpackages', views.AllPackageAPIView.as_view(), name='api-allpackages'),
        path('api/allpackagescount', views.PackageCountAPIView.as_view(), name='api-allpackagescount'),
        path('api/allpackages/<int:pk>', views.AllPackageDetailAPIView.as_view(), name='api-package-detail'),
        path('api/allpackages/<int:pk>/postreview', views.ReviewAPIView.as_view(), name='api-review-post'),
        path('api/activities/', views.TopActivitiesListAPIView.as_view(), name='api-activities'),
        path('api/activities/<int:pk>', views.TopActivitiesDetailsListAPIView.as_view(), name='api-activites_details'),

]

