from rest_framework import serializers
from .models import *

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopActivities
        fields = ['image', 'activity', 'description']



class PackageCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'package', 'full_name', 'review']



class PackageDetailSerializer(serializers.ModelSerializer):
    destination = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True)
    activities = ActivitiesSerializer (many=True)

    class Meta:
        model = Package
        fields = ['id', 'destination', 'package_name', 'image', 'duration', 'featured', 'content', 'highlights', 'inclusions', 'exclusions',
                  'image_1', 'image_2', 'image_3', 'itinerary',  'date_created', 'reviews', 'activities']



class PackageSerializer(serializers.ModelSerializer):
    #destination name instead of foreigen key id
    # destination = serializers.StringRelatedField()
    # destination = serializers.ReadOnlyField(source='destination.name')
    # url = serializers.HyperlinkedIdentityField(view_name='api-packages', read_only=True)
    activities = ActivitiesSerializer(many=True)
    class Meta:
        model = Package
        fields = ['id', 'destination', 'package_name', 'duration', 'featured', 'price', 'discount', 'discounted_price',
                            'savings', 'special_discount', 'rating', 'image', 'date_created', 'activities']
        # fields = '__all__'
        # depth = 1



class DestinationwithPackageSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many= True)
    class Meta:
        model = Destination
        fields = ['id', 'name', 'dest_image', 'packages']
        # fields = '__all__'
        # depth = 1





class DestinationFrontSerializer(serializers.ModelSerializer):
    #destination name instead of foreigen key id
    # destination = serializers.StringRelatedField()
    # destination = serializers.ReadOnlyField(source='destination.name')
    # url = serializers.HyperlinkedIdentityField(view_name='api-packages', read_only=True)
    # package = DestinationPackageSerializer(many= True)
    class Meta:
        model = Destination
        # fields = ['id', 'package']
        fields = '__all__'
        depth = 1


class AllpackageSerializer(serializers.ModelSerializer):
    class Meta:
        model =Package
        fields = ['id','destination', 'image', 'discount']











class TravelDealsSerializer(serializers.ModelSerializer):
    destination_name = serializers.ReadOnlyField(source='destination.name')
    class Meta:
        model = Package
        # fields = '__all__'
        fields = ['destination_name',]

class TopActivitiesSerializer(serializers.ModelSerializer):
    destination= serializers.StringRelatedField()
    class Meta:
        model = TopActivities
        fields = '__all__'

class TopAttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopAttractions
        fields = '__all__'

