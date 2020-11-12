from django.contrib import admin
from .models import *
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

    list_display = ('image_display', 'name', 'date_created',  'edit', 'delete')
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

    list_display = ('image_display','package_name', 'duration', 'featured', 'price', 'discounted_price',
                    'savings', 'special_discount', 'rating',
                    'content', 'highlights',  'image_1', 'image_2', 'image_3', 'itinerary','date_created', 'edit', 'delete')
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']
    icon_name = 'explore'

class ReviewAdmin(ModelAdmin):

    # autocomplete_fields = ['destination']

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/review/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/review/{}/delete/">Delete</a>', obj.id)

    list_display = ('full_name', 'review', 'created_at', 'edit', 'delete')
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']
    icon_name = 'layers'

@register(TopAttractions)
class TopAttractionsAdmin(ModelAdmin):
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/topattractions/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/topattractions/{}/delete/">Delete</a>', obj.id)

    list_display = ('image_display','title','edit', 'delete')
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']
    icon_name = 'layers'

@register(TopActivities)
class TopActivitiesAdmin(ModelAdmin):
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/topactivities/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/topactivities/{}/delete/">Delete</a>', obj.id)

    list_display = ('destination', 'image_display', 'title', 'description', 'edit', 'delete')
    # list_display = ('what','image_display', 'title', 'description', 'edit', 'delete')
    # list_filter = ('image_display', 'title', )
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']
    icon_name = 'layers'

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.site_header = 'Travel CRM'