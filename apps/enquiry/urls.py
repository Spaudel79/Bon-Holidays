# enquiry/urls.py
from django.urls import include, path
from rest_framework import routers
# from .views import ContactViewSet, FeedbackViewset
from django.urls import path, re_path, include
from .import views

# router = routers.DefaultRouter()
# router.register(r'contact', ContactViewSet)
# router.register(r'feedback', FeedbackViewset)
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [

        path('api/contactinfo', views.ContactListAPIView.as_view(), name='api-contactinfo'),
        path('api/contact/', views.ContactCreateAPIView.as_view(), name='api-contact'),
        # path('blog-post/<int:pk>', views.BlogPostDetailsListAPIView.as_view(), name='api-blog-post_details'),
        path('api/feedback/', views.FeedbackListAPIView.as_view(), name='api-comments'),


]