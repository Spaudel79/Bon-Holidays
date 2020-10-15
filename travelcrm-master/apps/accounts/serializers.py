# import token

from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User
from django.db.models import Q

class PartnerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerApplication
        fields = '__all__'

class BookmundiAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmundiAccount
        fields = '__all__'

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', ]

    def validate(self, attrs):
        # email = attrs.get('email', '')
        first_name = attrs.get ('first_name', '')

        if not first_name.isalnum():
            raise serializers.ValidationError('Enter only alnum')
        return attrs


    def create(self, validated_data):
         return User.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    email = serializers.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'email', 'password', 'token'
        ]
        extra_kwargs = {"password":
                            {"write_only":True}}

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data.get("password")
        if not email:
            raise serializers.ValidationError("Email is required for login")
        user = User.objects.filter(Q(email=email)).distinct()
        if user.exists() and user.count() ==1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This email is not valid/already exists")
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect password")
            data["token"] = "Random Token genereated"

        return data



