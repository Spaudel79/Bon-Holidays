from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class ChooseUs(models.Model):
    title = models.CharField(max_length=500,blank=True,null=True)
    description = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Why Choose Info"

class AboutUs(models.Model):
    welcome_title = models.CharField(max_length=500,blank=True)
    pic = models.ImageField(blank=True,null=True,verbose_name="Banner Image")
    welcome_description = models.TextField(blank=True,null=True)
    welcome_pic = models.ImageField(blank=True,null=True)
    happy_travellers = models.CharField(max_length=255,blank=True,null=True)
    satisfied_tours = models.CharField(max_length=255,blank=True,null=True)
    total_destination = models.CharField(max_length=255,blank=True,null=True)
    choose_info = models.ManyToManyField(ChooseUs,blank=True,null=True,verbose_name='Choose Info'
                                                                                    '(Add only three infos)')

    def __str__(self):
        return self.welcome_title

    class Meta:
        verbose_name_plural = "About Us Info"

class Testimonial(models.Model):
    full_name = models.CharField(max_length=255,blank=True,null=True)
    native_place = models.CharField(max_length=255,blank=True,null=True)
    pic = models.ImageField(blank=True,null=True)
    description = RichTextField(blank=True,null=True)
    tour_title = models.CharField(max_length=500, blank=True,null=True)
    rating = models.IntegerField(choices=((1, 1),
                                          (2, 2),
                                          (3, 3),
                                          (4, 4),
                                          (5, 5))
                                 )

    def __str__(self):
        return self.full_name

class Partner(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    pic = models.ImageField(blank=True, null=True, verbose_name="Banner Image")
    description = RichTextField(blank=True,null=True)
    join_title1 = models.CharField(max_length=255,blank=True,null=True)
    description_1 = RichTextField(blank=True,null=True)
    join_title2 = models.CharField(max_length=255, blank=True, null=True)
    description_2 = RichTextField(blank=True, null=True)
    join_title3 = models.CharField(max_length=255, blank=True, null=True)
    description_3 = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Partner Info"

class BecomePartner(models.Model):
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Potential Partners"


