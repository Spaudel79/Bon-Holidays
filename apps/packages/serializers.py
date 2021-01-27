from rest_framework import serializers
from .models import *

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopActivities
        fields = ['image', 'activity', 'description']


class NewActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewActivity
        fields = '__all__'

class PackageCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','full_name','user_rating', 'review']

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ['id', 'day', 'title', 'content']



class PackageDetailSerializer(serializers.ModelSerializer):
    destination = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True)
    activities = ActivitiesSerializer (many=True)


    class Meta:
        model = Package
        fields = ['id', 'destination', 'package_name', 'city', 'image', 'duration', 'featured', 'content', 'highlights', 'inclusions', 'exclusions',
                  'image_1', 'image_2', 'image_3', 'itinerary_text',  'date_created', 'reviews', 'activities']

        depth = 1



class PackageSerializer(serializers.ModelSerializer):
    #destination name instead of foreigen key id
    # destination = serializers.StringRelatedField()
    # destination = serializers.ReadOnlyField(source='destination.name')
    # url = serializers.HyperlinkedIdentityField(view_name='api-packages', read_only=True)
    # activities = ActivitiesSerializer(many=True)
    class Meta:
        model = Package
        fields = ['id', 'operator','destination', 'package_name', 'duration', 'featured', 'price', 'discount', 'discounted_price',
                   'city', 'tour_type','new_activity', 'accommodation', 'transport', 'age_range',
                  'savings', 'fix_departure', 'rating', 'image', 'date_created', ]
        # fields = '__all__'
        depth = 1



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

