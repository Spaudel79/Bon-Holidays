from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin, register
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html

# Register your models here.

@register(Logo)
class LogoAdmin(ModelAdmin):

    # search_fields = ['name']

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/logo/logo/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/logo/logo/{}/delete/">Delete</a>', obj.id)

    list_display = ('edit', 'delete')
    # image_display = AdminThumbnail(image_field='thumbnail')
    # image_display.short_description = 'Image'
    # readonly_fields = ['image_display']
    icon_name = 'spa'
