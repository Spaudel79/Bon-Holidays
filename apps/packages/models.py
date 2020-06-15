from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=255)
    duration = models.IntegerField(null=True)
    no_of_persons = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.destination}:{self.duration}:{self.price}"

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    package_name = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.IntegerField(choices=((1, 1),
                                          (2, 2),
                                          (3, 3),
                                          (4, 4),
                                          (5, 5))
                                 )
    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.package_name