from django.shortcuts import get_object_or_404
from .serializers import *
from django.core.mail import send_mail
from travel_crm.settings import EMAIL_HOST_USER

from .models import *
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
)

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated,
)

# Create your views here.


class BookingCreateAPIView(ListCreateAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):

        package = get_object_or_404(Package, pk=self.kwargs["pk"])
        serializer.save(package=package)

        name = serializer.data["name"]
        email = serializer.data["email"]
        phone = serializer.data["phone"]
        package = serializer.data["package"]
        bookedfor = serializer.data["bookedfor"]

        send_mail(
            "New Booking ",
            f"Booking Information\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Booked For: {bookedfor}\n"
            f"Package: {package}\n",
            email,
            [
                "sales6@bonholidays.com.np",
                "sales3@bonholidays.com.np",
                "sagar@bontravels.com",
                "ankur.aakashlabs@gmail.com",
                "shreya.aakashlabs@gmail.com",
            ],
            fail_silently=False,
        )


class BookingListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingListSerializer

    def get(self, request, *args, **kwargs):

        bookings = (
            Booking.objects.select_related("user", "package")
            .filter(user=request.user)
            .order_by("created_at")
        )

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
        people = serializer.data["people"]
        number_of_children = serializer.data["number_of_children"]
        number_of_adults = serializer.data["number_of_adults"]
        country = serializer.data["country"]
        bookedfor = serializer.data["bookedfor"]
        age_group = serializer.data["age_group"]
        tour_type = serializer.data["tour_type"]
        accomodation = serializer.data["accomodation"]
        budget = serializer.data["budget"]
        trip_stage = serializer.data["trip_stage"]
        send_mail(
            "New Custom Booking ",
            f" Custom Booking Information\n\n"
            f"First Name: {user.first_name}\n"
            f"Last Name: {user.last_name}\n"
            f"Email: {user.email}\n"
            f"PEOPLE CHOICES: {people}\n"
            f"No. of children: {number_of_children}\n"
            f"No. of adults: {number_of_adults}\n"
            f"Country of Package: {country}\n"
            f"Booked For: {bookedfor}\n"
            f"Age Group: {age_group}\n"
            f"Tour Type: {tour_type}\n"
            f"Accomodation: {accomodation}\n"
            f"Budget: {budget}\n"
            f"Trip Stage: {trip_stage}\n",
            EMAIL_HOST_USER,
            [
                "sales6@bonholidays.com.np",
                "sales3@bonholidays.com.np",
                "sagar@bontravels.com",
                "ankur.aakashlabs@gmail.com",
                "shreya.aakashlabs@gmail.com",
            ],
            fail_silently=False,
        )


class CustomBookingListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomBookingSerializer

    def get(self, request, *args, **kwargs):
        bookings = (
            CustomBooking.objects.select_related("user")
            .filter(user=request.user)
            .order_by("created_at")
        )
        serializer = self.get_serializer(bookings, many=True)
        return Response({"booking_history": serializer.data})
