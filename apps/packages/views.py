from rest_framework import viewsets, generics, filters
from .models import  *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
CreateAPIView, DestroyAPIView, ListCreateAPIView,
ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView
)
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
)

from django_filters import rest_framework as filters


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
    # queryset = Destination.objects.all().order_by('?')[:4]
    # queryset = Destination.objects.all().order_by('-date_created')[:4]
    queryset = Destination.objects.all()
    serializer_class = DestinationFrontSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['top', ]



class DestinationPackageListAPIView(RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationwithPackageSerializer



# class PackageFilter(filters.FilterSet):
#     activities = filters.CharFilter(
#         field_name='activities',
#         lookup_expr='contains'
#     )
#     class Meta:
#         model = Package
#         fields = ['featured', 'special_discount', 'activities']

class PackageAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class AllPackageAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    # filterset_class = PackageFilter

    # def get_queryset(self):
    #     # This might work with DjangoFilterBackend as well, don't know...
    #     activity = self.request.query_params.get('activity', None)
    #     if not activity:
    #         return Package.objects.all()
    #     else:
    #         return Package.objects.filter(activities__activity=activity)

    # def get_queryset(self):
    #     # This might work with DjangoFilterBackend as well, don't know...
    #     if self.request.query_params.get() is'featured':
    #         return Package.objects.filter(featured)
    #
    #     elif self.request.query_params.get() is 'special_discount':
    #             return Package.objects.filter(special_discount)
    def get_queryset(self):
        featured = self.request.query_params.get('featured', None)
        special_discount = self.request.query_params.get('special_discount', None)
        activity = self.request.query_params.get('activity', None)
        if featured is not None:
            return Package.objects.filter(featured=True)
        elif special_discount is not None:
            return Package.objects.filter(special_discount=True)
        elif activity is not None:
            return Package.objects.filter(activities__activity=activity)
        else:
            return Package.objects.all().order_by('-date_created')[:4]







class PackageCountAPIView(ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageCountSerializer
    # p_count = Package.objects.all().count()

    # def get_queryset(self):
    #         p_count=Package.objects.all().count()
    #         return[p_count]

    # def get_(self, request, *args, **kwargs):
    #     p_count = Package.objects.all().count()
    #     return self.list(request, {'p_count': p_count})

    # def get_queryset(self, *args, **kwargs):
    #
    #     p_count = Package.objects.all().count()
    #     return {'p_count': p_count}


class AllPackageDetailAPIView(RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageDetailSerializer

class ReviewAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # user = self.request.user
        package = get_object_or_404(Package, pk= self.kwargs['pk'])
        serializer.save(user=self.request.user,package=package)




class TopActivitiesListAPIView(ListAPIView):
    # queryset = TopActivities.objects.all().order_by('?')[:3]
    queryset = TopActivities.objects.all()
    serializer_class = TopActivitiesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
       'destination', 'activity'
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



