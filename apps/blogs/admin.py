from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/tag/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/tag/{}/delete/">Delete</a>', obj.id)

    list_display = ('tagname','edit', 'delete')
    icon_name = 'insert_link'



@register(BlogPost)
class BlogPostAdmin(ModelAdmin):


    # autocomplete_fields = ['author']
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/blogpost/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/blogpost/{}/delete/">Delete</a>', obj.id)

    list_display = ('categories', 'title', 'date_created','edit', 'delete')
    icon_name = 'chrome_reader_mode'
    # inlines = [TagInline]



    # class Media:
    #     js = ('ckeditor.js')

@register(Comment)
class CommentAdmin(ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/comment/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/blogs/comment/{}/delete/">Delete</a>', obj.id)

    list_display = ('blog','name', 'email', 'subject', 'created_at','edit', 'delete')
    icon_name = 'comment'



