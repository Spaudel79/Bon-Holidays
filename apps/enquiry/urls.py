# enquiry/urls.py
from django.urls import include, path
from rest_framework import routers
from .views import ContactViewSet, FeedbackViewset

router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet)
router.register(r'feedback', FeedbackViewset)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]