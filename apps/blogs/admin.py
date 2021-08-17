from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.admin import ModelAdmin, register
from django import forms
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

class BlogForm(forms.ModelForm):
    CATEGORY_CHOICES = (
        ('travel_news', 'Travel News',),
        ('travel_tips', 'Travel Tips',),
        ('things_to_do', 'Things to Do',),
        ('places_to_go', 'Places to Go'),
    )
    # categories = forms.MultipleChoiceField(choices = CATEGORY_CHOICES)

    class Meta:
        model = BlogPost
        fields = ['author','destination','image', 'title','categories',
                  'caption','content','tag','date_created']

    # def save(self, commit=True):
    #     data = self.cleaned_data
    #     blog = BlogPost(author = data['author'],
    #                     image = data['image'],
    #                     title = data['title'],
    #                     categories = data['categories'],
    #                     caption = data['caption'],
    #                     content = data['content'],
    #                     tag = data['tag'],
    #                     date_created = data['date_created'])
    #     blog.save()


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
    form = BlogForm



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

class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['email','date_subscribed']
    list_display_links = ['email']
    icon_name = 'sentiment_very_satisfied'


admin.site.register(Subscribers, SubscribersAdmin)

