from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.CharField(max_length=255, default="5% OFF")
    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __str__(self):
        return self.name

class Package(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.IntegerField(default=5)
    discount = models.CharField(max_length=255, default="15% OFF")
    discounted_price = models.IntegerField(default=230)
    savings = models.IntegerField(default=230)
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
    date_created = models.DateField()

    def __str__(self):
        return self.package_name