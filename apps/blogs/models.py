from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings
from apps.packages.models import *

# from django.contrib.auth import get_user_model
#
# User = get_user_model()


from django.db.models.signals import post_save


class Tag(models.Model):
    tagname = models.CharField(max_length=255)

    def __str__(self):
        return self.tagname


class BlogPost(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="blogpost",
    )
    author = models.CharField(max_length=64, default="Admin")
    CATEGORY_CHOICES = (
        (
            "travel_news",
            "Travel News",
        ),
        (
            "travel_tips",
            "Travel Tips",
        ),
        (
            "things_to_do",
            "Things to Do",
        ),
        ("places_to_go", "Places to Go"),
    )
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    categories = models.CharField(
        max_length=64, choices=CATEGORY_CHOICES, default="travel_news"
    )
    caption = models.CharField(max_length=500)
    content = RichTextUploadingField()

    # todo support for tags
    # tags = models.CharField(max_length=255, default='travel') #todo
    tag = models.ManyToManyField(Tag)
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


class Comment(models.Model):

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    blog = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    comment = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created_at",)


class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Newsletter Subscribers"

    # binding signal:
    @receiver(post_save, sender=BlogPost)
    def send_mails(sender, instance, created, **kwargs):
        subscribers = Subscribers.objects.all()

        if created:
            blog = BlogPost.objects.latest("date_created")
            for abc in subscribers:
                emailad = abc.email
                send_mail(
                    "New Blog Post ",
                    f" Checkout our new blog with title {blog.title} ",
                    settings.EMAIL_HOST_USER,
                    [emailad],
                    fail_silently=False,
                )
