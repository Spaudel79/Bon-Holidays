from django_filters import rest_framework as filters
from .models import *


class PackageFilter(filters.FilterSet):
    price = filters.RangeFilter()
    # destination__name = django_filters.MethodFilter()

    class Meta:
        model = Package
        fields = [
            "price",
            "featured",
            "fix_departure",
            "destinations__id",
            "destinations__name",
            "package_name",
        ]


class ContinentFilter(filters.FilterSet):
    class Meta:
        model = Destination
        fields = ["continent"]
