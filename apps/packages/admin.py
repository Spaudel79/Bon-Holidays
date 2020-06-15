from django.contrib import admin
from .models import Travel, Destination, Package
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Travel)
class TravelAdmin(ModelAdmin):
    list_display = ('destination', 'duration', 'price', 'date_created')
    icon_name = 'tram'

class DestinationAdmin(ModelAdmin):
    list_display = ('image', 'name', 'description', 'date_created')
    icon_name = 'tram'

class PackageAdmin(ModelAdmin):
    list_display = ('image', 'package_name', 'price', 'rating', 'date_created')
    icon_name = 'tram'

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.site_header = 'Travel CRM'

