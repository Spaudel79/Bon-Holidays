from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile
from django.contrib.admin import ModelAdmin
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

admin.site.register(User, UsersAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


