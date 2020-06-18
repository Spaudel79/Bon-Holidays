# # packages/urls.py


# packages/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'partner-application', views.PartnerApplicationViewSet)
router.register(r'bookmundi-account', views.BookmundiAccountViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]







# from django.urls import include, path
# from django.conf.urls import url
# from . import views
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
# ]
#
# app_name = 'accounts'