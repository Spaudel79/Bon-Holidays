from rest_framework import serializers
from .models import Package, Destination, TopActivities, TopAttractions

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

class TopActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopActivities
        fields = '__all__'

class TopAttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopAttractions
        fields = '__all__'

