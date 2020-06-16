from rest_framework import serializers
from .models import Package, Destination

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
