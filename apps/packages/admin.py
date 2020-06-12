from django.contrib import admin
from .models import Travel
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Travel)
class TravelAdmin(ModelAdmin):
    list_display = ('destination', 'duration', 'price', 'date_created')
    icon_name = 'tram'


admin.site.site_header = 'Travel CRM'

