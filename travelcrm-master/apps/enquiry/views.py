from rest_framework import viewsets, mixins
from .models import  *
from .serializers import *
from rest_framework.generics import (
CreateAPIView, DestroyAPIView,
ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView
)

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
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer

class FeedbackListAPIView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer