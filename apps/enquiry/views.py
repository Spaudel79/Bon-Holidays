from rest_framework import viewsets, mixins
from .models import  *
from .serializers import *
from rest_framework.generics import (
CreateAPIView, DestroyAPIView,
ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView
)
from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
)
from django.core.mail import send_mail
from travel_crm.settings import EMAIL_HOST_USER

# class ContactViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
# class FeedbackViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer


class ContactListAPIView(ListAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactInfoSerializer

class ContactCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        name = serializer.data['full_name']
        email = serializer.data['email']
        subject = serializer.data['subject']
        send_mail('New Contact ', f"Contact has been made by {name} "
                                  f"having email {email} "
                                  f"and subject {subject}",
                  email, ['saroj.aakashlabs@gmail.com'],
                  fail_silently=False)

class FeedbackListAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        name = serializer.data['name']
        email = serializer.data['email']
        subject = serializer.data['subject']
        send_mail('New Feedback ', f"Feedback has been given by {name} "
                                  f"having email {email} "
                                  f"and subject {subject}",
                  email, ['saroj.aakashlabs@gmail.com'],
                  fail_silently=False)