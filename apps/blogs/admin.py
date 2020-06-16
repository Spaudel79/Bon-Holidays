from django.contrib import admin
from .models import BlogPost
from django.utils.html import format_html
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(BlogPost)
class BlogPostAdmin(ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/blogpost/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/blogpost/{}/delete/">Delete</a>', obj.id)

    list_display = ('name', 'html_stripped', 'edit', 'delete')
    icon_name = 'assignment'
