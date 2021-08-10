from rest_framework import serializers
from .models import *
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
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            "password": {"write_only": True},
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        email = attrs.get('email')

        if first_name:
            if not first_name.isalnum():
                raise serializers.ValidationError('Enter only alphanumeric value for first name')

        if last_name:
            if not last_name.isalnum():
                raise serializers.ValidationError('Enter only alphanumeric value for last name')


        #email = unique already provided in the model
        # user = User.objects.filter(Q(email=email)).distinct()
        # if user.exists() and user.count() == 1:
        #     raise serializers.ValidationError('User hello with this email already exists')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    # token = serializers.CharField(allow_blank=True, read_only=True)
    email = serializers.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'id', 'email', 'password',
        ]
        # fields = '__all__'
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
        if user.exists() and user.count() == 1:
            user = user.first()
        else:
            raise serializers.ValidationError("This email is not valid")
        if user:
            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect password")

        data['user'] = user
        return data


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['group', 'user', 'commission', 'last_updated']
        depth = 1




