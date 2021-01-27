from rest_framework import viewsets, generics, filters
from .models import  *
from .serializers import *
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .filter import PackageFilter, ContinentFilter
from django.http import QueryDict
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
from django.core.mail import send_mail
from travel_crm.settings import EMAIL_HOST_USER

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
    queryset = Destination.objects.all().order_by('-date_created')

    serializer_class = DestinationFrontSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['top', 'continent' ]
    # filterset_class = ContinentFilter #filterset_class and filterset_fields dont work together


class DestinationPackageListAPIView(RetrieveAPIView):
    queryset = Destination.objects.all()
    # queryset = Destination.objects.annotate(package_count=Count('package'))
    serializer_class = DestinationwithPackageSerializer


class PackageAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class AllPackageAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filterset_class = PackageFilter

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
    # def get_queryset(self):
    #     featured = self.request.query_params.get('featured', None)
    #     fix_departure = self.request.query_params.get('fix_departure', None)
    #     activity = self.request.query_params.get('activity', None)
    #     if featured is not None:
    #         return Package.objects.filter(featured=True)
    #     elif fix_departure is not None:
    #         return Package.objects.filter(fix_departure=True)
    #     # elif activity is not None:
    #     #     return Package.objects.filter(activities__activity=activity)
    #     else:
    #         return Package.objects.all().order_by('-date_created')[:4]
    # def get_queryset(self):
    #     operator = self.request.GET.get("operator", None)
    #     if operator is not None:
    #         operator = self.request.GET.get("operator", "")
    #         operator_values = operator.split(",")
    #         return Package.objects.filter(operator__company_name__in=operator_values)
    #     else:
    #         return Package.objects.all()

#Actual Filtering starts
    def get_queryset(self):
        new_activity = self.request.GET.get('new_activity',None)
        tour_type = self.request.GET.get("tour_type",None)
        operator = self.request.GET.get("operator", None)
        if new_activity is not None:
            new_activity = self.request.GET.get('new_activity', "")
            new_activity_values = new_activity.split(",")
            if tour_type is not None:
                    tour_type = self.request.GET.get("tour_type", "")
                    tour_type_values = tour_type.split(",")
                    if operator is not None:
                        operator = self.request.GET.get("operator", "")
                        operator_values = operator.split(",")
                        return Package.objects.filter(new_activity__title__in=new_activity_values,
                                              tour_type__in=tour_type_values,
                                                  operator__in=operator_values)
                    else:
                        return Package.objects.filter(new_activity__title__in=new_activity_values,
                                                  tour_type__in=tour_type_values,)
            elif operator is not None:
                    operator = self.request.GET.get("operator", "")
                    operator_values = operator.split(",")
                    if tour_type is not None:
                        tour_type = self.request.GET.get("tour_type", "")
                        tour_type_values = tour_type.split(",")
                        return Package.objects.filter(new_activity__title__in=new_activity_values,
                                                      tour_type__in=tour_type_values,
                                                      operator__company_name__in=operator_values)
                    else:
                        return Package.objects.filter(new_activity__title__in=new_activity_values,
                                                      operator__company_name__in=operator_values)
            else:
                    return Package.objects.filter(new_activity__title__in=new_activity_values,)

        elif tour_type is not None:
            tour_type = self.request.GET.get("tour_type", "")
            tour_type_values = tour_type.split(",")
            if operator is not None:
                operator = self.request.GET.get("operator", "")
                operator_values = operator.split(",")
                if new_activity is not None:
                    new_activity = self.request.GET.get('new_activity', "")
                    new_activity_values = new_activity.split(",")
                    return Package.objects.filter(new_activity__title__in=new_activity_values,
                                                  tour_type__in=tour_type_values,
                                                  operator__company_name__in=operator_values)
                else:
                    return Package.objects.filter(tour_type__in=tour_type_values,
                                                  operator__company_name__in=operator_values)
            elif new_activity is not None:
                new_activity = self.request.GET.get('new_activity', "")
                new_activity_values = new_activity.split(",")
                if operator is not None:
                    operator = self.request.GET.get("operator", "")
                    operator_values = operator.split(",")
                    return Package.objects.filter(new_activity__title__in=new_activity_values,
                                                  tour_type__in=tour_type_values,
                                                  operator__company_name__in=operator_values)
                else:
                    return Package.objects.filter(tour_type__in=tour_type_values,
                                                  new_activity__title__in=new_activity_values,)
            else:
                return Package.objects.filter(tour_type__in=tour_type_values,)
        elif operator is not None:
            operator = self.request.GET.get("operator", "")
            operator_values = operator.split(",")
            if new_activity is not None:
                new_activity = self.request.GET.get('new_activity', "")
                new_activity_values = new_activity.split(",")
                if tour_type is not None:
                    tour_type = self.request.GET.get("tour_type", "")
                    tour_type_values = tour_type.split(",")
                    return Package.objects.filter(new_activity__title__in=new_activity_values,
                                                  tour_type__in=tour_type_values,
                                                  operator__company_name__in=operator_values)
                else:
                    return Package.objects.filter(new_activity__title__in=new_activity_values,
                                                  operator__company_name__in=operator_values)
            elif tour_type is not None:
                tour_type = self.request.GET.get("tour_type", "")
                tour_type_values = tour_type.split(",")
                if new_activity is not None:
                    new_activity = self.request.GET.get('new_activity', "")
                    new_activity_values = new_activity.split(",")
                    return Package.objects.filter(new_activity__title__in=new_activity_values,
                                                  tour_type__in=tour_type_values,
                                                  operator__company_name__in=operator_values)
                else:
                    return Package.objects.filter(tour_type__in=tour_type_values,
                                                  operator__company_name__in=operator_values)
            else:
                return Package.objects.filter(operator__company_name__in=operator_values)
        return Package.objects.all()

# Actual Filtering Ends


    # def list(self, request, format=None, *args, **kwargs):
    #
    #     new_activity = self.request.query_params.get('new_activity', "")
    #     destination = self.request.query_params.get("destination", "")
    #     destination_values = destination.split(",")
    #     new_activity_values = new_activity.split(",")
    #     if new_activity is not None:
    #         if destination is not None:
    #             queryset = Package.objects.filter(destination__name__in=destination_values,
    #                                           new_activity__title__in=new_activity_values)
    #             serializer = self.get_serializer(queryset, many=True)
    #             return Response(serializer.data)
    #         else:
    #             queryset = Package.objects.filter(new_activity__title__in=new_activity_values)
    #             serializer = self.get_serializer(queryset, many=True)
    #             return Response(serializer.data)
    #     elif destination is not None:
    #         if new_activity is not None:
    #             queryset = Package.objects.filter(destination__name__in=destination_values,
    #                                           new_activity__title__in=new_activity_values)
    #             serializer = self.get_serializer(queryset, many=True)
    #             return Response(serializer.data)
    #         else:
    #             queryset = Package.objects.filter(destination__name__in=destination_values)
    #             serializer = self.get_serializer(queryset, many=True)
    #             return Response(serializer.data)
    #     else:
    #         queryset = Package.objects.all()
    #         serializer = self.get_serializer(queryset, many=True)
    #         return Response(serializer.data)
    # def get(self, request, format=None, *args, **kwargs):
    #     dict_params = dict(request.query_params.iterlists())
    #     filter = PackageFilter(dict_params, queryset=Package.objects.all())



class PackageCountAPIView(ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageCountSerializer
    # p_count = Package.objects.all().count()

    def get_queryset(self):
        p_count=Package.objects.all().count()
        return[p_count]

    # def get_(self, request, *args, **kwargs):
    #     p_count = Package.objects.all().count()
    #     return self.list(request, {'p_count': p_count})

    # def get_queryset(self):
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

        name = serializer.data['full_name']


        send_mail('New Review ', f"Review has been made by {name}"

                  ,EMAIL_HOST_USER, ['sales6@bonholidays.com.np'],
                  fail_silently=False)




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

class NewActivityListAPIView(ListAPIView):
    queryset = NewActivity.objects.all()
    serializer_class = NewActivitySerializer



