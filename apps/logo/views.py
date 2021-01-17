from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView

# Create your views here.

class LogoAPIView(ListAPIView):
    queryset = Logo.objects.all().order_by('-date_created')[:1]
    serializer_class = LogoSerializer