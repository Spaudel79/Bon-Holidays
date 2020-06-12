from django.contrib import admin
from .models import BlogPost
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('name',)
    # icon_name = ''
