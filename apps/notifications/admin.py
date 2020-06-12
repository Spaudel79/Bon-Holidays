from django.contrib import admin
from .models import Notification
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display = ('name',)
    # icon_name = ''
