from django.contrib import admin
from .models import Destination, Package
from django.contrib.admin import ModelAdmin, register
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html
# Register your models here.


class DestinationAdmin(ModelAdmin):

    search_fields = ['name']

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/destination/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/destination/{}/delete/">Delete</a>', obj.id)

    list_display = ('image_display', 'name', 'description', 'discount', 'edit', 'delete')
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']
    icon_name = 'explore'

class PackageAdmin(ModelAdmin):

    autocomplete_fields = ['destination']

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/package/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/package/{}/delete/">Delete</a>', obj.id)

    list_display = ('image_display','package_name', 'duration', 'price', 'discounted_price', 'savings',  'rating', 'date_created', 'edit', 'delete')
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']
    icon_name = 'layers'

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.site_header = 'Travel CRM'

