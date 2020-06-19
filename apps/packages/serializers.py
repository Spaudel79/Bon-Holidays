from rest_framework import serializers
from .models import Package, Destination

class PackageSerializer(serializers.ModelSerializer):
    #destination name instead of foreigen key id
    destination_name = serializers.ReadOnlyField(source='destination.name')
    class Meta:
        model = Package
        fields = ['destination_name', 'package_name', 'price', 'rating', 'image', 'date_created']

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'