from rest_framework import serializers
from .models import BookmundiAccount, PartnerApplication

class PartnerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerApplication
        fields = '__all__'

class BookmundiAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmundiAccount
        fields = '__all__'