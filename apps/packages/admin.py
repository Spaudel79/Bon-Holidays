from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin, register
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html
from apps.accounts.models import User, UserProfile

# Register your models here.


class DestinationAdmin(ModelAdmin):

    search_fields = ['name']

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/destination/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/destination/{}/delete/">Delete</a>', obj.id)

    list_display = ('name', 'continent', 'top', 'date_created',  'edit', 'delete')
    # image_display = AdminThumbnail(image_field='thumbnail')
    # image_display.short_description = 'Image'
    # readonly_fields = ['image_display']
    icon_name = 'explore'

    def changelist_view(self, request, extra_context=None):
        if not request.user.is_superuser:
            self.list_display = ('name', 'top', 'continent', 'date_created',)
        else:
            self.list_display = ('name', 'top', 'continent', 'date_created',  'edit', 'delete')
        return super(DestinationAdmin, self).changelist_view(request, extra_context)



class PackageAdmin(ModelAdmin):
    icon_name = 'explore'
    # autocomplete_fields = ['destination']

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/package/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/package/{}/delete/">Delete</a>', obj.id)

    list_display = ('package_name',  'featured', 'price',
                     'fix_departure', 'rating',
                     'date_created', 'edit', 'delete')

    # image_display = AdminThumbnail(image_field='thumbnail')
    # image_display.short_description = 'Image'
    # readonly_fields = ['image_display']



    def get_queryset(self, request):
        abc = super(PackageAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return abc
        else:
            operator = request.user.profile
            return abc.filter(operator=operator)

    # class Media:
    #     js = ('ckeditor.js','configuration-ckeditor.js')

@register(Review)
class ReviewAdmin(ModelAdmin):

    # autocomplete_fields = ['author']
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/package/review/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/package/review/{}/delete/">Delete</a>', obj.id)

    list_display = ('user', 'package', 'user_rating', 'full_name', 'created_at', 'edit', 'delete')
    icon_name = 'assignment'

# @register(TopAttractions)
# class TopAttractionsAdmin(ModelAdmin):
#     def edit(self, obj):
#         return format_html('<a class="btn-btn" href="/admin/packages/topattractions/{}/change/">Change</a>', obj.id)
#
#     def delete(self, obj):
#         return format_html('<a class="btn-btn" href="/admin/packages/topattractions/{}/delete/">Delete</a>', obj.id)
#
#     list_display = ('image_display','title','edit', 'delete')
#     image_display = AdminThumbnail(image_field='thumbnail')
#     image_display.short_description = 'Image'
#     readonly_fields = ['image_display']
#     icon_name = 'layers'

# @register(TopActivities)
# class TopActivitiesAdmin(ModelAdmin):
#     def edit(self, obj):
#         return format_html('<a class="btn-btn" href="/admin/packages/topactivities/{}/change/">Change</a>', obj.id)
#
#     def delete(self, obj):
#         return format_html('<a class="btn-btn" href="/admin/packages/topactivities/{}/delete/">Delete</a>', obj.id)
#
#     list_display = ( 'image_display', 'activity',  'edit', 'delete')
#     # list_display = ('what','image_display', 'title', 'description', 'edit', 'delete')
#     # list_filter = ('image_display', 'title', )
#     image_display = AdminThumbnail(image_field='thumbnail')
#     image_display.short_description = 'Image'
#     readonly_fields = ['image_display']
#     icon_name = 'layers'

@register(NewActivity)
class NewActivityAdmin(ModelAdmin):
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/newactivity/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/packages/newactivity/{}/delete/">Delete</a>', obj.id)

    list_display = ('title',  'edit', 'delete')
    icon_name = 'layers'

# class PackageInline(admin.TabularInline):
#     model = Package
#     exclude = [ 'featured', 'price', 'discounted_price',
#                     'savings', 'special_discount',
#                      ]


admin.site.register(Destination, DestinationAdmin)
admin.site.register(Package, PackageAdmin)
# admin.site.register(Itinerary)

admin.site.site_header = 'Bon Holidays'