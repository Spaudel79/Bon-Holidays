from rest_framework import viewsets
from .models import  Destination, Package
from .serializers import PackageSerializer

class PackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer