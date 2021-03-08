from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView
from .models import *

# Create your views here.

class TestimonialAPIView(ListAPIView):
    queryset = Testimonial.objects.all().order_by('-id')[:1]
    serializer_class = TestimonialSerializer

class AboutUsAPIView(ListAPIView):
    queryset = AboutUs.objects.all().order_by('-id')[:1]
    serializer_class = AboutUsSerializer
