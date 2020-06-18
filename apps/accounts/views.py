from rest_framework import viewsets, mixins
from .models import  PartnerApplication, BookmundiAccount
from .serializers import PartnerApplicationSerializer, BookmundiAccountSerializer

class PartnerApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = PartnerApplication.objects.all()
    serializer_class = PartnerApplicationSerializer

class BookmundiAccountViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = BookmundiAccount.objects.all()
    serializer_class = BookmundiAccountSerializer
























# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from django.views.generic import DetailView, ListView, UpdateView
#
# from .models import UserProfile
#
# @login_required
# def profile_redirector(request):
#     return redirect('accounts:userprofile', username=request.user.email)