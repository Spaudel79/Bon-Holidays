from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework.generics import (
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


class BookingCreateAPIView(CreateAPIView):
    # permission_classes= [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # def perform_create(self, serializer):
    #     # user = self.request.user
    #     package = get_object_or_404(Booking, pk= self.kwargs['pk'])
    #     serializer.save(package=package)

    def create(self, request, *args, **kwargs):
        booking_data = request.data
        new_booking = Booking.objects.create(user=booking_data["user"],
                                             package=booking_data["package"],
                                             name=booking_data["name"],
                                             email=booking_data["email"],
                                             phone=booking_data["phone"],
                                             bookedfor=booking_data["bookedfor"],
                                             created_at = booking_data["created_at"]

                                             )
        new_booking.save()
        serializer = BookingSerializer(new_booking)
        return Response(serializer.data,status=status.HTTP_200_OK)

