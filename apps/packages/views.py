from rest_framework import viewsets, generics, filters
from .models import  Destination, Package
from .serializers import PackageSerializer

class PackageViewSet(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['destination__name','date_created']
    ordering_fields = ['date_created']