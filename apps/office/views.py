from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import *
from rest_framework.permissions import AllowAny

# Create your views here.


class TestimonialAPIView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class AboutUsAPIView(ListAPIView):
    queryset = AboutUs.objects.all().order_by("-id")[:1]
    serializer_class = AboutUsSerializer


class PartnerAPIView(ListAPIView):
    queryset = Partner.objects.all().order_by("-id")[:1]
    serializer_class = PartnerSerializer


class BecomePartnerAPIView(CreateAPIView):
    # permission_classes = [AllowAny]
    queryset = BecomePartner.objects.all()
    serializer_class = BecomePartnerSerializer
