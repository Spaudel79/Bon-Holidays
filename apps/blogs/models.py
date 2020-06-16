from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class BlogPost(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def __str__(self):
        return self.name

    @property
    def html_stripped(self):
       from django.utils.html import strip_tags
       return strip_tags(self.content)