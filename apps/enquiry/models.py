from django.db import models

# Create your models here.

class Contact(models.Model):
    address = models.CharField(max_length=255, default="795 Australia")
    phone = models.CharField(max_length=255, default="808 - 808")
    email = models.EmailField(default="hello@hello.com")
    description = models.TextField(null=True, blank=True)
    opened_till = models.CharField(max_length=255, default="Mondey to Sunday")

    def __str__(self):
        return self.address


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(null=True)


