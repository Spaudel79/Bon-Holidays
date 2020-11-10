from rest_framework import serializers
from .serializers import *
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'bookedfor']