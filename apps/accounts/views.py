from rest_framework import viewsets, mixins, response,status
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *
from django.contrib.auth.models import Permission
from rest_framework.generics import (GenericAPIView,
CreateAPIView, DestroyAPIView,
ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView
)

class PartnerApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = PartnerApplication.objects.all()
    serializer_class = PartnerApplicationSerializer

class BookmundiAccountViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = BookmundiAccount.objects.all()
    serializer_class = BookmundiAccountSerializer


class RegisterUserView(GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self,request):
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
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            return response.Response(new_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

























# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from django.views.generic import DetailView, ListView, UpdateView
#
# from .models import UserProfile
#
# @login_required
# def profile_redirector(request):
#     return redirect('accounts:userprofile', username=request.user.email)