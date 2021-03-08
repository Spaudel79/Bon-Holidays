from django.urls import path, re_path, include
from .import views



urlpatterns = [

        path('api/testimonial', views.TestimonialAPIView.as_view(), name='api-testimonial'),
        path('api/aboutus', views.AboutUsAPIView.as_view(), name='api-aboutus'),


]