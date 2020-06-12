from django.contrib import admin
from .models import Destination
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Destination)
class DestinationAdmin(ModelAdmin):
    list_display = ('name',)
    # icon_name = ''
