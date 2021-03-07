from django.db import models
from ckeditor.fields import RichTextField
#import datetime
from datetime import datetime

# Create your models here.

# class AddressInfo(models.Model):
#     full_address = models.CharField(max_length=255,blank=True,null=True)

class AddressInfo(models.Model):
    full_address = models.CharField(max_length=255)

    def __str__(self):
        return self.full_address

class Contact(models.Model):

    #address = models.CharField(max_length=255, default="795 Australia")
    address = models.ManyToManyField(AddressInfo,blank=True,null=True)
    phone = models.CharField(max_length=255, default="808 - 808")
    email = models.EmailField(default="hello@hello.com")
    description = RichTextField(blank=True)
    opened_till = models.CharField(max_length=255, default="Mondey to Sunday")
    date_created = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.date_created


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
