from rest_framework import serializers
from .serializers import *
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'bookedfor']
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
        fields = [ 'people', 'number_of_children', 'number_of_adults', 'geographical_area',
                    'age_group', 'tour_type', 'accomodation', 'budget', 'budget_flexibility', 'Trip_stage',
                     'trip_title', 'description','bookedfor',]