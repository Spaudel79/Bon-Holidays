from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(BlogPost)
class BlogPostAdmin(ModelAdmin):

    # autocomplete_fields = ['author']
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/blogpost/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/blogpost/{}/delete/">Delete</a>', obj.id)

    list_display = ('categories', 'html_stripped', 'title', 'date_created','edit', 'delete')
    icon_name = 'assignment'

@register(Comment)
class CommentAdmin(ModelAdmin):

    list_display = ('name', 'email', 'subject', 'comment', 'created_at')
    icon_name = 'comment'