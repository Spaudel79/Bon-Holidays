from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView

# Create your views here.

class LogoAPIView(ListAPIView):

    queryset = Logo.objects.all()
    serializer_class = LogoSerializer