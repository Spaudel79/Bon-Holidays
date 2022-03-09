from django_filters import rest_framework as filters
from .models import *


class PackageFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Package
        fields = ["price", "featured", "fix_departure", "destination__id"]

    # def filter_first_filter(self, queryset, value):
    #     # I expect value to setup with an array of values
    #     myquery = Q()
    #     return queryset.filter(myquery)


class ContinentFilter(filters.FilterSet):
    class Meta:
        model = Destination
        fields = ["continent"]
