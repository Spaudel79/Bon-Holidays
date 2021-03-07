from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin, register
# Register your models here.

@register(ChooseUs)
class ChooseUsAdmin(ModelAdmin):
    icon_name = 'feedback'

@register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('welcome_title','happy_travellers','total_destination')
    icon_name = 'feedback'