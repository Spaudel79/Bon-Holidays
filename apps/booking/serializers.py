from rest_framework import serializers
from .serializers import *
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    package = serializers.CharField(read_only=True)
    class Meta:
        model = Booking
        fields = ['id','name','package', 'email', 'phone', 'bookedfor']
        # fields = '__all__'

class BookingListSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = Booking

        fields = '__all__'
        depth = 1

class CustomBookingSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = CustomBooking
        fields = ['id', 'people', 'number_of_children', 'number_of_adults','country','bookedfor',
                    'age_group', 'tour_type', 'accomodation', 'budget',  'trip_stage',
                     ]