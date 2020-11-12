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

    def post(self, request):
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
        # return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Logout(GenericAPIView):
#     def get(self, request, format=None):
#         auth.logout(request)
#         return Response(status=status.HTTP_200_OK)


class Logout(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# class Logout(GenericAPIView):
#     def logout(self, request):
#         try:
#             request.user.auth_token.delete()
#         except (AttributeError, ObjectDoesNotExist):
#             pass
#
#         # django_logout(request)
#         return Response(status=status.HTTP_200_OK)

# class UsersListView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer


class UsersListView(ListAPIView):
    # serializer_class = UserListSerializer

    # def get(self, request, *args, **kwargs):
    #     user = Token.objects.get(key="token").user
    #     # if user.exists():
    #     #     user =user.last().user
    #     return self.list(request, user)

    def get(self, request, *args, **kwargs):
        serializer = UserListSerializer(request.user)
        return Response({"user": serializer.data})

    # def get_queryset(self):
    #
    #
    #     user_id = Token.objects.get(key=self.request.auth.key).user_id
    #     return User.objects.filter(user=User.objects.get(id=user_id))
    #     # return self.list(self.request, user)






    # def get_queryset(self):
    #     # user = Token.objects.get(key="token")
    #     # return User.objects.filter(user= user)
    #     return User.objects.filter(user =Token.objects.get(key="token").user)

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         user = serializer.object.get('user') or request.user
    #         token = serializer.object.get('token')
    #         response_data = {
    #             'token': token,
    #             'user': UserListSerializer(user).data
    #         }
    #         response = Response(response_data, status=status.HTTP_200_OK)

# class UsersListView(ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer
#
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)






























# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from django.views.generic import DetailView, ListView, UpdateView
#
# from .models import UserProfile
#
# @login_required
# def profile_redirector(request):
#     return redirect('accounts:userprofile', username=request.user.email)