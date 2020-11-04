from rest_framework import viewsets, generics, filters
from .models import  *
from .serializers import *
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
CreateAPIView, DestroyAPIView,
ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView
)
from django_filters.rest_framework import DjangoFilterBackend

# class DestinationViewSet(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
#     queryset = Destination.objects.all()
#     serializer_class = DestinationSerializer
#
# class PackageViewSet(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
#     queryset = Package.objects.all()
#     serializer_class = PackageSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['destination__name','date_created']
#     ordering_fields = ['date_created']
#
# class TopActtractionsViewset(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
#     queryset = TopAttractions.objects.all()
#     serializer_class = TopAttractionsSerializer
#
# class TopActivitiesViewset(generics.ListAPIView, generics.RetrieveAPIView, viewsets.GenericViewSet):
#     queryset = TopActivities.objects.all()
#     serializer_class = TopActivitiesSerializer

class DestinationFrontListAPIView(ListAPIView):
    queryset = Destination.objects.all().order_by('?')[:4]
    # queryset = Package.objects.all().order_by('-date_created')[:4]
    serializer_class = DestinationFrontSerializer



class DestinationPackageListAPIView(RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationwithPackageSerializer


class AllPackageAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['featured', 'special_discount']

class AllPackageDetailAPIView(RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageDetailSerializer


class TopActivitiesListAPIView(ListAPIView):
    # queryset = TopActivities.objects.all().order_by('?')[:3]
    queryset = TopActivities.objects.all()
    serializer_class = TopActivitiesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
       'destination', 'title',
    ]

    # def get_queryset(self):
    #     """
    #     This view should return a list of all models by
    #     the maker passed in the URL
    #     """
    #     maker = self.kwargs['destination']
    #     return TopActivities.objects.filter(destination=maker)



    # def get_queryset(self, *args, **kwargs):
    #     queryset = TopActivities.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset = queryset.filter(
    #             Q(destination__icontains=query)|Q(title__icontains=query))
    #     return queryset


class TopActivitiesDetailsListAPIView(RetrieveAPIView):
    queryset = TopActivities.objects.all()
    serializer_class = TopActivitiesSerializer



