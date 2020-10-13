from django.db import models
from ckeditor.fields import RichTextField
from apps.accounts.models import *
from ckeditor_uploader.fields import RichTextUploadingField

class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('travel_news', 'Travel News',),
        ('travel_tips', 'Travel Tips',),
        ('things_to_do', 'Things to Do',),
        ('places_to_go', 'Places to Go'),
    )
    image = models.ImageField(blank=True, null=True)
    categories = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='travel_news')
    description = models.CharField(max_length=255)
    content = RichTextUploadingField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # todo support for tags
    tags = models.CharField(max_length=255, default='#travel') #todo
    date_created = models.DateField()

    @property
    def html_stripped(self):
       from django.utils.html import strip_tags
       return strip_tags(self.content)

class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    comment = models.TextField()
    # jpt = models.CharField(max_length=255)