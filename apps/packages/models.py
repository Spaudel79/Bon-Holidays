from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# from django_random_queryset import RandomManager
from ckeditor.fields import RichTextField
from apps.accounts.models import UserProfile, User
from image_cropping.fields import ImageRatioField, ImageCropField


class Destination(models.Model):
    Continent_Name = (
        (
            "Europe",
            "Europe",
        ),
        (
            "Asia",
            "Asia",
        ),
        (
            "North America",
            "North America",
        ),
        (
            "South America",
            "South America",
        ),
        (
            "Africa",
            "Africa",
        ),
        (
            "Oceania",
            "Oceania",
        ),
        (
            "Polar",
            "Polar",
        ),
        (
            "Regions",
            "Regions",
        ),
    )
    name = models.CharField(max_length=255, unique=True)
    continent = models.CharField(
        max_length=255, choices=Continent_Name, default="Europe"
    )
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

    class Meta:
        ordering = ("-id",)

    @property
    def locations(self):
        total_list = list(self.packages.values_list("city", flat=True))
        return total_list

    @classmethod
    def get_all_locations(cls):
        total_list = list(cls.objects.all().values_list("name", flat=True))
        return total_list

    def all_locations(self):
        ls1 = self.locations
        ls2 = self.get_all_locations()

        ls = (
            ls1
            + ls2
            + [
                "Europe",
                "Asia",
                "North America",
                "South America",
                "Africa",
                "Oceania",
                "Polar",
                "Regions",
            ]
        )

        return ls


class Itinerary(models.Model):
    day = models.IntegerField()
    title = models.CharField(max_length=255)
    content = RichTextField()

    def __str__(self):
        return f"Day{self.day}:{self.title}"


class NewActivity(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        # verbose_name = "New Activity"
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title


class Package(models.Model):
    TOUR_TYPE = (
        (
            "Custom-made trip with guide and/or driver",
            "Custom-made trip with guide and/or driver",
        ),
        (
            "Custom-made trip without guide and driver",
            "Custom-made trip without guide and driver",
        ),
        (
            "Group Tour",
            "Group Tour",
        ),
        (
            "Cruise Tour",
            "Cruise Tour",
        ),
    )

    operator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    price = models.IntegerField(verbose_name="Price in Nrs")
    price_2 = models.IntegerField(verbose_name="Price in $")
    duration = models.IntegerField(default=5)
    duration_hours = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Hours If One day Tour"
    )
    discount = models.IntegerField(verbose_name="Discount %", default=15)
    tour_type = models.CharField(
        max_length=100, choices=TOUR_TYPE, default="Group Tour"
    )
    new_activity = models.ManyToManyField(NewActivity)
    accommodation = models.CharField(max_length=255, default="Guest House & Hotel")
    transport = models.CharField(max_length=150, default="Flight")
    age_range = models.CharField(max_length=100, default="6 to 79 years old")
    fix_departure = models.BooleanField(default=False)
    rating = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))

    image = models.ImageField(blank=True, verbose_name="Thumbnail Image-Vertical")
    # thumbnail = ImageSpecField(source='image',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})
    content = RichTextField()
    highlights = RichTextField()
    inclusions = RichTextField()
    exclusions = RichTextField()

    itinerary_text = RichTextField()
    faqs = RichTextField(blank=True)
    image_1 = models.ImageField(blank=True, null=True, verbose_name="Image-Horizontal")
    image_2 = models.ImageField(blank=True, null=True, verbose_name="Image-Square")
    image_3 = models.ImageField(blank=True, null=True, verbose_name="Image-Sqaure")
    date_created = models.DateField()

    def __str__(self):
        return self.package_name

    class Meta:
        ordering = ("-id",)


class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="reviews"
    )
    user_rating = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    full_name = models.CharField(max_length=255)
    review = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ("created_at",)


class TopAttractions(models.Model):

    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class TopActivities(models.Model):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="activities"
    )

    image = models.ImageField(blank=True)
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
    activity = models.CharField(max_length=64)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.activity
