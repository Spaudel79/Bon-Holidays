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
    destinations = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True)
    activities = ActivitiesSerializer (many=True)


    class Meta:
        model = Package
        fields = ['id', 'destinations', 'package_name', 'city', 'image', 'duration',
                  'featured','price','price_2', 'discount','faqs','duration_hours',
                  'content', 'highlights', 'inclusions', 'exclusions',
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
        fields = ['id', 'operator','destinations', 'package_name', 'duration', 'featured', 'price','price_2', 'discount',
                   'city', 'tour_type','new_activity', 'accommodation', 'transport', 'age_range',
                   'fix_departure', 'rating', 'image', 'date_created', ]
        # fields = '__all__'
        depth = 1



class DestinationwithPackageSerializer(serializers.ModelSerializer):
    packages = PackageDetailSerializer(many= True)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'dest_image', 'packages'  ]
        # fields = '__all__'
        # depth = 1

# class Destinationwith

class DestinationFrontSerializer(serializers.ModelSerializer):
    #destination name instead of foreigen key id
    # destination = serializers.StringRelatedField()
    # destination = serializers.ReadOnlyField(source='destination.name')
    # url = serializers.HyperlinkedIdentityField(view_name='api-packages', read_only=True)
    # package = DestinationPackageSerializer(many= True)
    # packages = PackageSerializer(many=True)
    packages_count = serializers.IntegerField()
    class Meta:
        model = Destination
        # fields = ['id', 'package']
        fields = ['packages_count','id', 'name', 'dest_image','continent','top',]
        # depth = 1


class AllpackageSerializer(serializers.ModelSerializer):
    class Meta:
        model =Package
        fields = ['id','destinations', 'image', 'discount']

class TravelDealsSerializer(serializers.ModelSerializer):
    destination_name = serializers.ReadOnlyField(source='destinations.name')
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

