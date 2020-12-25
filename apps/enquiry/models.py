from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Contact(models.Model):

    address = models.CharField(max_length=255, default="795 Australia")
    phone = models.CharField(max_length=255, default="808 - 808")
    email = models.EmailField(default="hello@hello.com")
    description = RichTextField(blank=True)
    opened_till = models.CharField(max_length=255, default="Mondey to Sunday")

    def __str__(self):
        return self.address


class ContactForm(models.Model):
    contacted = models.BooleanField(default=False)
    subject = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(default="hello@hello.com")
    description = RichTextField(blank=True)


    def __str__(self):
        return self.full_name


class Feedback(models.Model):
    contacted = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = RichTextField(blank=True)

# class About(models.Model):
