from rest_framework import viewsets
from .models import Travel, Destination, Package
from .serializers import TravelSerializer, PackageSerializer

class TravelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class PackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer