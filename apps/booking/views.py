from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from apps.packages.models import Package
from django.http import HttpResponse
from django.core.mail import send_mail
from travel_crm.settings import EMAIL_HOST_USER

from .models import *
from rest_framework.generics import (ListCreateAPIView,
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
    #permission_classes= [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # user = self.request.user
        package = get_object_or_404(Package, pk= self.kwargs['pk'])
        serializer.save(package=package)
        # data = self.request.data
        name = serializer.data['name']
        email = serializer.data['email']
        phone = serializer.data['phone']

        send_mail('New Booking ',f"Booking has been made by {name} "
                                 f"having email {email} "
                                 f"and phone number {phone}",
                  email , ['sales6@bonholidays.com.np','sales3@bonholidays.com.np','sagar@bontravels.com'],
                  fail_silently=False)

        # send_mail('New Booking ', f"Booking has been made by {name} "
        #                           f"having email {email} "
        #                           f"and phone number {phone}",
        #           email, ['shreya.aakashlabs@gmail.com'],
        #           fail_silently=False)

    # def send_email(request):
    #     email = ('New booking is created')
    #     email.send()

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

class CustomBookingCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomBooking.objects.all()
    serializer_class = CustomBookingSerializer

    def perform_create(self, serializer):
        user = self.request.user
        # package = get_object_or_404(Package, pk= self.kwargs['pk'])
        serializer.save(user=user)

        send_mail('New Custom Booking ', f" Custom Booking has been made by {user.first_name} {user.last_name} "
                                  f"having email {user.email} "
                                  ,
                  EMAIL_HOST_USER, ['sales6@bonholidays.com.np','sales3@bonholidays.com.np','sagar@bontravels.com'],
                  fail_silently=False)

class CustomBookingListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomBookingSerializer

    def get(self, request, *args, **kwargs):
        bookings = CustomBooking.objects.filter(user=request.user).order_by('created_at')
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
    #     serializer = self.get_serializer(bookings, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # user = booking_data["user"],

