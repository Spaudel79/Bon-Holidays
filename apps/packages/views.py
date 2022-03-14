from rest_framework import viewsets, generics, filters
from .models import *
from .serializers import *
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from django.db.models import Q
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)

from .filter import PackageFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import (
    IsAuthenticated,
)
from django.core.mail import send_mail
from travel_crm.settings import EMAIL_HOST_USER


class DestinationFrontListAPIView(ListAPIView):
    queryset = (
        Destination.objects.all()
        .order_by("-date_created")
        .annotate(packages_count=Count("packages"))
    )
    serializer_class = DestinationFrontSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["top", "continent"]

    def get(self, request, *args, **kwargs):

        search = self.request.query_params.get("search", None)

        if search is not None:
            qs = (
                Package.objects.select_related("operator")
                .prefetch_related("destinations", "new_activity")
                .filter(
                    Q(destinations__name__icontains=search)
                    | Q(destinations__continent__icontains=search)
                    | Q(package_name__icontains=search)
                    | Q(city__icontains=search)
                )
                .distinct()
            )
            serializer = PackageSerializer(qs, many=True)
            return Response(serializer.data, status=200)

        qs = self.get_queryset().prefetch_related("packages")
        serializer = self.get_serializer(qs, many=True)
        additional_field = {"locations": qs[0].all_locations()}
        return Response([additional_field, serializer.data], status=200)


class DestinationPackageListAPIView(RetrieveAPIView):
    queryset = Destination.objects.prefetch_related("packages")
    serializer_class = DestinationwithPackageSerializer


class PackageCountView(ListAPIView):
    queryset = Destination.objects.annotate(packages_count=Count("packages"))
    serializer_class = DestinationwithPackageSerializer


class PackageAPIView(ListAPIView):
    queryset = Package.objects.select_related("operator").prefetch_related(
        "destinations", "new_activity"
    )
    serializer_class = PackageSerializer


class AllPackageAPIView(ListAPIView):
    queryset = Package.objects.select_related("operator").prefetch_related(
        "destinations", "new_activity"
    )
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
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
                else:
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                    )
                    return qs
            elif operator is not None:
                operator = self.request.GET.get("operator", "")
                operator_values = operator.split(",")
                if tour_type is not None:
                    tour_type = self.request.GET.get("tour_type", "")
                    tour_type_values = tour_type.split(",")
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
                else:
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
            else:
                qs = self.queryset.filter(
                    new_activity__title__in=new_activity_values,
                )
                return qs

        elif tour_type is not None:
            tour_type = self.request.GET.get("tour_type", "")
            tour_type_values = tour_type.split(",")
            if operator is not None:
                operator = self.request.GET.get("operator", "")
                operator_values = operator.split(",")
                if new_activity is not None:
                    new_activity = self.request.GET.get("new_activity", "")
                    new_activity_values = new_activity.split(",")
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
                else:
                    qs = self.queryset.filter(
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
            elif new_activity is not None:
                new_activity = self.request.GET.get("new_activity", "")
                new_activity_values = new_activity.split(",")
                if operator is not None:
                    operator = self.request.GET.get("operator", "")
                    operator_values = operator.split(",")
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
                else:
                    qs = self.queryset.filter(
                        tour_type__in=tour_type_values,
                        new_activity__title__in=new_activity_values,
                    )
                    return qs
            else:
                qs = self.queryset.filter(
                    tour_type__in=tour_type_values,
                )
                return qs
        elif operator is not None:
            operator = self.request.GET.get("operator", "")
            operator_values = operator.split(",")
            if new_activity is not None:
                new_activity = self.request.GET.get("new_activity", "")
                new_activity_values = new_activity.split(",")
                if tour_type is not None:
                    tour_type = self.request.GET.get("tour_type", "")
                    tour_type_values = tour_type.split(",")
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
                else:
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
            elif tour_type is not None:
                tour_type = self.request.GET.get("tour_type", "")
                tour_type_values = tour_type.split(",")
                if new_activity is not None:
                    new_activity = self.request.GET.get("new_activity", "")
                    new_activity_values = new_activity.split(",")
                    qs = self.queryset.filter(
                        new_activity__title__in=new_activity_values,
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
                else:
                    qs = self.queryset.filter(
                        tour_type__in=tour_type_values,
                        operator__company_name__in=operator_values,
                    )
                    return qs
            else:
                qs = self.queryset.filter(operator__company_name__in=operator_values)
                return qs
        return self.queryset


class PackageCountAPIView(ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageCountSerializer

    def get_queryset(self):
        p_count = Package.objects.all().count()
        return [p_count]


class AllPackageDetailAPIView(RetrieveAPIView):
    queryset = Package.objects.select_related("operator").prefetch_related(
        "destinations", "new_activity"
    )
    serializer_class = PackageDetailSerializer


class ReviewAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):

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

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset().select_related("user", "package")
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=200)


class NewActivityListAPIView(ListAPIView):
    queryset = NewActivity.objects.all()
    serializer_class = NewActivitySerializer
