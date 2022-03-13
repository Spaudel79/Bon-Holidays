from rest_framework import serializers
from .models import *


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopActivities
        fields = ["image", "activity", "description"]


class NewActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewActivity
        fields = "__all__"


class PackageCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "full_name", "user_rating", "review"]


class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ["id", "day", "title", "content"]


class PackageDetailSerializer(serializers.ModelSerializer):
    destinations = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True)
    activities = ActivitiesSerializer(many=True)

    class Meta:
        model = Package
        fields = [
            "id",
            "destinations",
            "package_name",
            "city",
            "image",
            "duration",
            "featured",
            "price",
            "price_2",
            "discount",
            "faqs",
            "duration_hours",
            "content",
            "highlights",
            "inclusions",
            "exclusions",
            "image_1",
            "image_2",
            "image_3",
            "itinerary_text",
            "date_created",
            "reviews",
            "activities",
        ]

        depth = 1


class PackageSerializer(serializers.ModelSerializer):

    operator = serializers.StringRelatedField()
    destinations = serializers.StringRelatedField()

    class Meta:
        model = Package
        fields = [
            "id",
            "operator",
            "destinations",
            "package_name",
            "duration",
            "featured",
            "price",
            "price_2",
            "discount",
            "city",
            "tour_type",
            "new_activity",
            "accommodation",
            "transport",
            "age_range",
            "fix_departure",
            "rating",
            "image",
            "date_created",
        ]

        depth = 1


class DestinationwithPackageSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True)

    class Meta:
        model = Destination
        fields = ["id", "name", "dest_image", "packages"]


# class Destinationwith


class DestinationFrontSerializer(serializers.ModelSerializer):

    packages_count = serializers.IntegerField()

    class Meta:
        model = Destination
        fields = ["packages_count", "id", "name", "dest_image", "continent", "top"]


class AllpackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["id", "destinations", "image", "discount"]


class TravelDealsSerializer(serializers.ModelSerializer):
    destination_name = serializers.ReadOnlyField(source="destinations.name")

    class Meta:
        model = Package
        # fields = '__all__'
        fields = [
            "destinations_name",
        ]


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = "__all__"


class CityNameSerializer(serializers.ModelSerializer):

    destination = serializers.StringRelatedField()

    class Meta:
        model = Package
        fields = [
            "id",
            "destinations",
            "package_name",
            "duration",
            "featured",
            "city",
            "tour_type",
            "accommodation",
            "transport",
            "age_range",
            "fix_departure",
        ]
