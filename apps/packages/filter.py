from django_filters import rest_framework as filters
from .models import *


class PackageFilter(filters.FilterSet):
   price = filters.RangeFilter()

   class Meta:
      model = Package
      fields = ['price','featured', 'fix_departure',
                'tour_type',]
