from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# from django_random_queryset import RandomManager
from ckeditor.fields import RichTextField
from apps.accounts.models import UserProfile, User

class Destination(models.Model):
    # Continent_Name = (
    #     ('Europe, 'Custom-made trip with guide and/or driver',),
    #     ('Asia', 'Custom-made trip without guide and driver',),
    #     ('North America, 'Group Tour',),
    #     ('South America', 'Cruise Tour',),
    #     ('Africa', 'Cruise Tour',),
    #     ('South America', 'Cruise Tour',),
    # )
    name = models.CharField(max_length=255, unique=True)
    # continent = models.CharField(max_length=255, unique=True)
    top = models.BooleanField(default=False)
    dest_image = models.ImageField(blank=True)
    # thumbnail = ImageSpecField(source='dest_image',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})

    def __str__(self):
        return self.name

    @property
    def packages(self):
        return self.package_set.all()

    date_created = models.DateField()

class Itinerary(models.Model):
    day = models.IntegerField()
    title = models.CharField(max_length=255)
    content = RichTextField()

    def __str__(self):
        return f'Day{self.day}:{self.title}'


class NewActivity(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        # verbose_name = "New Activity"
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title

class Package(models.Model):
    TOUR_TYPE = (
        ('Custom-made trip with guide and/or driver', 'Custom-made trip with guide and/or driver',),
        ('Custom-made trip without guide and driver', 'Custom-made trip without guide and driver',),
        ('Group Tour', 'Group Tour',),
        ('Cruise Tour', 'Cruise Tour',),
    )

    operator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    price = models.IntegerField()
    duration = models.IntegerField(default=5)
    discount = models.CharField(max_length=255, default="15% OFF")
    discounted_price = models.IntegerField(default=230)
    savings = models.IntegerField(default=230)
    tour_type = models.CharField(max_length=100, choices=TOUR_TYPE, default='Group Tour')
    new_activity = models.ManyToManyField(NewActivity)
    accommodation = models.CharField(max_length=255,default='Guest House & Hotel')
    transport = models.CharField(max_length=150, default='Flight')
    age_range = models.CharField(max_length=100, default='6 to 79 years old')
    fix_departure = models.BooleanField(default=False)
    rating = models.IntegerField(choices=((1, 1),
                                          (2, 2),
                                          (3, 3),
                                          (4, 4),
                                          (5, 5))
                                 )

    image = models.ImageField(blank=True)
    # thumbnail = ImageSpecField(source='image',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})
    content =RichTextField()
    highlights = RichTextField()
    inclusions = RichTextField()
    exclusions = RichTextField()
    # itinerary = models.ManyToManyField(Itinerary)
    itinerary_text = RichTextField()
    image_1= models.ImageField(blank=True,null = True)
    image_2= models.ImageField(blank=True,null = True)
    image_3= models.ImageField(blank=True,null = True)
    date_created = models.DateField()


    def __str__(self):
        return self.package_name

    # def is_featured(self):
    #     return self.featured



class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='reviews')
    user_rating = models.IntegerField(choices=((1, 1),
                                          (2, 2),
                                          (3, 3),
                                          (4, 4),
                                          (5, 5))
                                 )
    full_name = models.CharField(max_length=255)
    review = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

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
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='activities')


    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    activity = models.CharField(max_length=64)
    description =RichTextField(blank=True)


    def __str__(self):
        return self.activity