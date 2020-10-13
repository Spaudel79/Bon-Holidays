from django.contrib import admin
from .models import Contact, Feedback
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('address', 'phone', 'email', 'description')
    icon_name = 'call'

@register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    icon_name = 'feedback'