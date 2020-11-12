from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# from django_random_queryset import RandomManager
from ckeditor.fields import RichTextField

class Destination(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # description = models.CharField(max_length=255)
    # discount = models.CharField(max_length=255, default="5% OFF")
    # featured = models.BooleanField(default=False)
    dest_image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(source='dest_image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __str__(self):
        return self.name

    @property
    def packages(self):
        return self.package_set.all()

    date_created = models.DateField()


class Package(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    price = models.IntegerField()
    duration = models.IntegerField(default=5)
    discount = models.CharField(max_length=255, default="15% OFF")
    discounted_price = models.IntegerField(default=230)
    savings = models.IntegerField(default=230)
    special_discount = models.BooleanField(default=False)
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
    content =RichTextField()
    highlights = RichTextField()
    itinerary = RichTextField()
    image_1= models.ImageField(blank=True,null = True)
    image_2= models.ImageField(blank=True,null = True)
    image_3= models.ImageField(blank=True,null = True)
    date_created = models.DateField()


    def __str__(self):
        return self.package_name

    # def is_featured(self):
    #     return self.featured

class Review(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='review')
    full_name = models.CharField(max_length=255)
    review = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('created_at',)

class TopAttractions(models.Model):

    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class TopActivities(models.Model):

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title