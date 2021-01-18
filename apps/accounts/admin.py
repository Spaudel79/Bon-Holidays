from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import * #UserGroup
from django.contrib.admin import ModelAdmin
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html
from django.utils.translation import gettext as _

from django.contrib.auth.models import Group


from apps.accounts import models
# Register your models here.
class UsersAdmin(UserAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/accounts/user/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/accounts/user/{}/delete/">Delete</a>', obj.id)

    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'edit', 'delete']
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'groups', 'is_staff')}),
        ('Important dates', {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    icon_name = 'person'




class UserProfileAdmin(ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/accounts/userprofile/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/accounts/userprofile/{}/delete/">Delete</a>', obj.id)

    icon_name = 'person_pin'
    search_fields = ['first_name','last_name','phone_number', 'company_name']
    autocomplete_fields = ['user']

    list_display = ('image_display', 'user', 'group', 'user_type','first_name',
                     'last_updated', 'edit', 'delete')
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']


#already commented out
# class UserGroupAdmin(ModelAdmin):
#     icon_name = 'people'


# class PartnerApplicationAdmin(ModelAdmin):
#     list_display = ('first_name', 'last_name', 'company_name', 'email_address', 'phone', 'state')
#     icon_name = 'people'
#
# class BookmundiAccountAdmin(ModelAdmin):
#     list_display = ('title', 'first_name', 'middle_name', 'last_name',
#                     'date_of_birth', 'nationality', 'occupation', 'email',
#                     'phone_number', 'passport_number', 'expiry_date')
#     icon_name = 'person'

admin.site.register(User, UsersAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# #already commented out
# # admin.site.register(UserGroup, UserGroupAdmin)
# # admin.site.unregister(Group)
#
# admin.site.register(PartnerApplication, PartnerApplicationAdmin)
# admin.site.register(BookmundiAccount, BookmundiAccountAdmin)
