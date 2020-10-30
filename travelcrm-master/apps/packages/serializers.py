from rest_framework import serializers
from .models import *

class PackageSerializer(serializers.ModelSerializer):
    #destination name instead of foreigen key id
    destination_name = serializers.ReadOnlyField(source='destination.name')
    class Meta:
        model = Package
        # fields = ['destination_name', 'package_name', 'price', 'rating', 'image', 'date_created']
        fields = '__all__'

class DestinationFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        # fields = '__all__'
        fields = ['id', 'name', 'image']

class TopActivitiesSerializer(serializers.ModelSerializer):
    destination= serializers.StringRelatedField()
    class Meta:
        model = TopActivities
        fields = '__all__'

class TopAttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopAttractions
        fields = '__all__'

