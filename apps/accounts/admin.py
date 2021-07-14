from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.admin import ModelAdmin
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html


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

    def get_queryset(self, request):
        abc = super(UserProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return abc
        else:
            user = request.user.id
            return abc.filter(user=user)




admin.site.register(User, UsersAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
