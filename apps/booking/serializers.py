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