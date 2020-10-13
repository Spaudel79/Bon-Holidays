from rest_framework import viewsets, mixins
from .models import  Contact, Feedback
from .serializers import ContactSerializer, FeedbackSerializer

class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class FeedbackViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer