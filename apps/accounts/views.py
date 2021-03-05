from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, mixins, response, status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated
from django.contrib import auth
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly,
)
from rest_framework.authentication import TokenAuthentication

from .models import *
from .serializers import *
from django.contrib.auth.models import Permission
from rest_framework.generics import (GenericAPIView,
CreateAPIView, DestroyAPIView, ListCreateAPIView,
ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class Homepage(GenericAPIView):
    def get(self,request):
        return Response(status=status.HTTP_200_OK)


class PartnerApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = PartnerApplication.objects.all()
    serializer_class = PartnerApplicationSerializer


class BookmundiAccountViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = BookmundiAccount.objects.all()
    serializer_class = BookmundiAccountSerializer


class RegisterUserView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request, **kwargs):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return response.Response(user_data, status=status.HTTP_201_CREATED)


class LoginUserView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        new_data = serializer.data
        user = serializer.validated_data["user"]
        serializer = self.get_serializer(user)
        token, created = Token.objects.get_or_create(user=user)
        # return response.Response(new_data, status=status.HTTP_200_OK)
        return response.Response({"token": token.key,
                                  "serializer.data": serializer.data},
                                   status=status.HTTP_200_OK)


class Logout(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UsersListView(ListAPIView):
    def get(self, request, *args, **kwargs):
        serializer = UserListSerializer(request.user)
        return Response({"user": serializer.data})


class ProfileListView(ListAPIView):
    # permission_classes = [AllowAny]
    serializer_class = ProfileListSerializer
    queryset = UserProfile.objects.all()






























# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from django.views.generic import DetailView, ListView, UpdateView
#
# from .models import UserProfile
#
# @login_required
# def profile_redirector(request):
#     return redirect('accounts:userprofile', username=request.user.email)