from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from apps.packages.models import Package
from django.http import HttpResponse

from .models import *
from rest_framework.generics import ( ListCreateAPIView,
CreateAPIView, DestroyAPIView,
ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView
)
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
)

# Create your views here.


class BookingCreateAPIView(ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # user = self.request.user
        package = get_object_or_404(Package, pk= self.kwargs['pk'])
        serializer.save(user=self.request.user,package=package)

class BookingListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Booking.objects.all()
    serializer_class = BookingListSerializer


    def get(self, request,*args, **kwargs):
    #     bookings = Booking.objects.get(user=request.user)
    #     return HttpResponse(bookings)

        # bookings = Booking.objects.order_by('created_at')
        bookings = Booking.objects.filter(user=request.user).order_by('created_at')
        # return HttpResponse(bookings)
        serializer = self.get_serializer(bookings, many=True)
        return Response({"booking_history": serializer.data})



    # def get_queryset(self):
    #     return Booking.objects.filter(user=self.user)

    # def list(self, request, *args, **kwargs):
    #
    #     queryset = Booking.objects.get(user=request.user)
    #     # serializer = self.get_serializer(queryset, many=True)
    #     return Response({"queryset": queryset})


    # def create(self, request, *args, **kwargs):
    #     booking_data = request.data
    #     new_booking = Booking.objects.create(
    #                                          package=booking_data["package"],
    #                                          name=booking_data["name"],
    #                                          email=booking_data["email"],
    #                                          phone=booking_data["phone"],
    #                                          bookedfor=booking_data["bookedfor"],
    #                                          created_at = booking_data["created_at"]
    #
    #                                          )
    #     new_booking.save()
    #     serializer = BookingSerializer(new_booking)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # user = booking_data["user"],

