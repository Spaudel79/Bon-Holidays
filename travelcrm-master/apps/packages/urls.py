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

        path('api/destinations', views.DestinationListAPIView.as_view(), name='api-destinations'),

        path('api/packages', views.PackageListAPIView.as_view(), name='api-packages'),
        path('api/packages/<int:pk>', views.PackageDetailsListAPIView.as_view(), name='api-packages_details'),
        path('api/activities/', views.TopActivitiesListAPIView.as_view(), name='api-activities'),
        path('api/activities/<int:pk>', views.TopActivitiesDetailsListAPIView.as_view(), name='api-activites_details'),

]

