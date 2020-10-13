from rest_framework import viewsets, generics, filters
from .models import  Destination, Package, TopAttractions, TopActivities
from .serializers import PackageSerializer, DestinationSerializer, TopActivitiesSerializer, TopAttractionsSerializer

class DestinationViewSet(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class PackageViewSet(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['destination__name','date_created']
    ordering_fields = ['date_created']

class TopActtractionsViewset(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = TopAttractions.objects.all()
    serializer_class = TopAttractionsSerializer

class TopActivitiesViewset(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
    queryset = TopActivities.objects.all()
    serializer_class = TopActivitiesSerializer