from rest_framework import serializers
from .models import *

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'