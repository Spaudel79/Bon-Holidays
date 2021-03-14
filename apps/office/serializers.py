from rest_framework import serializers
from .models import *

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
        depth = 1

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
        depth = 1

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
        depth = 1

class BecomePartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomePartner
        fields = '__all__'
