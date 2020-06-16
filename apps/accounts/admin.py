from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile
from django.contrib.admin import ModelAdmin
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html
from django.utils.translation import gettext as _

from apps.accounts import models
# Register your models here.
class UsersAdmin(UserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    icon_name = 'person'




class UserProfileAdmin(ModelAdmin):
    icon_name = 'person_pin'
    search_fields = ['user__name']
    autocomplete_fields = ['user']

    list_display = ('image_display', 'about', 'user_type', 'last_updated')
    image_display = AdminThumbnail(image_field='thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']

admin.site.register(User, UsersAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


