from django.contrib import admin
from .models import Contact
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name',)
    # icon_name = ''