from rest_framework import viewsets, generics, filters
from .models import *
from .serializers import *
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .filter import PackageFilter, ContinentFilter
from django.http import QueryDict
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
)
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from django.core.mail import send_mail
from travel_crm.settings import EMAIL_HOST_USER
from rest_framework import status

from django_filters import rest_framework as filters


class DestinationFrontListAPIView(ListAPIView):
    queryset = (
        Destination.objects.all()
        .order_by("-date_created")
        .annotate(packages_count=Count("package"))
    )
    serializer_class = DestinationFrontSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["top", "continent"]

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset().prefetch_related("package_set")

        serializer = self.get_serializer(qs, many=True)
        additional_field = {"locations": qs[0].all_locations()}
        return Response([additional_field, serializer.data], status=200)


class DestinationPackageListAPIView(RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationwithPackageSerializer


class PackageCountView(ListAPIView):
    queryset = Destination.objects.annotate(packages_count=Count("package"))
    serializer_class = DestinationwithPackageSerializer


class PackageAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class AllPackageAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filterset_class = PackageFilter

    # Actual Filtering starts
    def get_queryset(self):
        new_activity = self.request.GET.get("new_activity", None)
        tour_type = self.request.GET.get("tour_type", None)
        operator = self.request.GET.get("operator", None)
        if new_activity is not None:
            new_activity = self.request.GET.get("new_activity", "")
            new_activity_values = new_activity.split(",")
            if tour_type is not None:
                tour_type = self.request.GET.get("tour_type", "")
                tour_type_values = tour_type.split(",")
                if operator is not None:
                    operator = self.request.GET.get("operator", "")
                    operator_values = operator.split(",")
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                else:
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                    )
            elif operator is not None:
                operator = self.request.GET.get("operator", "")
                operator_values = operator.split(",")
                if tour_type is not None:
                    tour_type = self.request.GET.get("tour_type", "")
                    tour_type_values = tour_type.split(",")
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                else:
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        operator__company_name__in=operator_values,
                    )
            else:
                return Package.objects.filter(
                    new_activity__title__in=new_activity_values,
                )

        elif tour_type is not None:
            tour_type = self.request.GET.get("tour_type", "")
            tour_type_values = tour_type.split(",")
            if operator is not None:
                operator = self.request.GET.get("operator", "")
                operator_values = operator.split(",")
                if new_activity is not None:
                    new_activity = self.request.GET.get("new_activity", "")
                    new_activity_values = new_activity.split(",")
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                else:
                    return Package.objects.filter(
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
            elif new_activity is not None:
                new_activity = self.request.GET.get("new_activity", "")
                new_activity_values = new_activity.split(",")
                if operator is not None:
                    operator = self.request.GET.get("operator", "")
                    operator_values = operator.split(",")
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                else:
                    return Package.objects.filter(
                        tour_type__in=tour_type_values,
                        new_activity__title__in=new_activity_values,
                    )
            else:
                return Package.objects.filter(
                    tour_type__in=tour_type_values,
                )
        elif operator is not None:
            operator = self.request.GET.get("operator", "")
            operator_values = operator.split(",")
            if new_activity is not None:
                new_activity = self.request.GET.get("new_activity", "")
                new_activity_values = new_activity.split(",")
                if tour_type is not None:
                    tour_type = self.request.GET.get("tour_type", "")
                    tour_type_values = tour_type.split(",")
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                else:
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        operator__company_name__in=operator_values,
                    )
            elif tour_type is not None:
                tour_type = self.request.GET.get("tour_type", "")
                tour_type_values = tour_type.split(",")
                if new_activity is not None:
                    new_activity = self.request.GET.get("new_activity", "")
                    new_activity_values = new_activity.split(",")
                    return Package.objects.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                else:
                    return Package.objects.filter(
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
            else:
                return Package.objects.filter(
                    operator__company_name__in=operator_values
                )
        return Package.objects.all()


class PackageCountAPIView(ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageCountSerializer

    def get_queryset(self):
        p_count = Package.objects.all().count()
        return [p_count]


class AllPackageDetailAPIView(RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageDetailSerializer


class ReviewAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # user = self.request.user
        package = get_object_or_404(Package, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, package=package)

        name = serializer.data["full_name"]
        send_mail(
            "New Review ",
            f"Review has been made by {name}",
            EMAIL_HOST_USER,
            ["sales6@bonholidays.com.np"],
            fail_silently=False,
        )


class NewActivityListAPIView(ListAPIView):
    queryset = NewActivity.objects.all()
    serializer_class = NewActivitySerializer


class PackageSearchAPi(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def get(self, request, *args, **kwargs):

        search = self.request.query_params.get("search", None)
        if search is not None:
            qs = Package.objects.filter(
                Q(destination__name__icontains=search)
                | Q(destination__continent__icontains=search)
                | Q(package_name__icontains=search)
                | Q(city__icontains=search)
            ).disctinct()

        else:
            qs = Package.objects.values(
                "id", "destination", "package_name", "city"
            ).distinct()

        serializer = CityNameSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
