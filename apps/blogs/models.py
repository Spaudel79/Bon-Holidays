from django.db import models
from ckeditor.fields import RichTextField
from apps.accounts.models import UserProfile, User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    author = models.CharField(max_length=64, default='Admin')
    CATEGORY_CHOICES = (
        ('travel_news', 'Travel News',),
        ('travel_tips', 'Travel Tips',),
        ('things_to_do', 'Things to Do',),
        ('places_to_go', 'Places to Go'),
    )
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    categories = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='travel_news')
    caption = models.CharField(max_length=500)
    content = RichTextUploadingField()

    # todo support for tags
    tags = models.CharField(max_length=255, default='travel') #todo
    date_created = models.DateField()

    @property
    def html_stripped(self):
       from django.utils.html import strip_tags
       return strip_tags(self.content)

    def __str__(self):
        return self.title

    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type

    # @property
    # def comments(self):
    #     return self.comments_set.all()

class Comment(models.Model):
    # blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    comment = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_at',)



    # def __str__(self):
    #     return f'Comment by {self.author.username} on {self.post}'

    # jpt = models.CharField(max_length=255)