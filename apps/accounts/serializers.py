# import token

from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate

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
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
                        "password":{"write_only": True},
                        'first_name':{'required': False},
                        'last_name':{'required': False}
                       }

    def validate(self, attrs):
        # email = attrs.get('email', '')
        first_name = attrs.get ('first_name', '')
        last_name = attrs.get ('last_name', '')

        if first_name:
            if not first_name.isalnum():
                raise serializers.ValidationError('Enter only alphanumeric value for first name')

        if last_name:
            if not last_name.isalnum():
                raise serializers.ValidationError('Enter only alphanumeric value for last name')

        return attrs
        # if not email:
        #     raise serializers.ValidationError("Email is required for login")
        # if not password:
        #     raise serializers.ValidationError("Password is required for login")


    def create(self, validated_data):
         return User.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.ModelSerializer):
    # token = serializers.CharField(allow_blank=True, read_only=True)
    email = serializers.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'email', 'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}}

    def validate(self, data):
        user = None
        email = data.get("email", None)
        password = data.get("password")
        if not email:
            raise serializers.ValidationError("Email is required for login")
        if not password:
            raise serializers.ValidationError("Password is required for login")
        user = User.objects.filter(Q(email=email)).distinct()
        if user.exists() and user.count() ==1:
            user = user.first()
        else:
            raise serializers.ValidationError("This email is not valid")
        if user:
            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect password")


        # user = authenticate(email=email, password=password)
        # if not user:
        #     raise serializers.ValidationError("Invalid email or password")


        # if not user.check_password(password):
        #     raise serializers.ValidationError("Incorrect password")

        data['user'] = user

        return data
        # data["token"] = "Random Token genereated"





