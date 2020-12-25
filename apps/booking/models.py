from django.db import models
from apps.accounts.models import UserProfile, User
from apps.packages.models import Package
from ckeditor.fields import RichTextField

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package')
    contacted = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    bookedfor = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('created_at',)

class Test(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='test')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    new = RichTextField()



class CustomBooking(models.Model):
    PEOPLE_CHOICES = (
            ('Single', 'Single',),
            ('Couple', 'Couple',),
            ('Family', 'Family',),
            ('Group', 'Group'),
        )
    AGE_GROUP = (
            ('18-35 yrs', '18-35 yrs',),
            ('36-50 yrs', '36-50 yrs',),
            ('51-64 yrs', '51-64 yrs',),
            ('65+ yrs', '65+ yrs',),
        )
    TOUR_TYPE = (
            ('Custom-made trip with guide and/or driver', 'Custom-made trip with guide and/or driver',),
            ('Custom-made trip without guide and driver', 'Custom-made trip without guide and driver',),
            ('Group Tour', 'Group Tour',),
            ('Cruise Tour', 'Cruise Tour',),
        )
    ACCOMODATIONS = (
        ('Basic', 'Basic',),
        ('Comfortable', 'Comfortable',),
        ('Luxury', 'Luxury',),
        ('Quirky', 'Quirky',),
    )
    # FLEXIBILITY = (
    #     ('No,this is my maximum budget', 'No,this is my maximum budget',),
    #     ('Flexible,I can increase up to 20%,if needed', 'Flexible,I can increase up to 20%,if needed',),
    #     ('Very flexible, plan me the best trip possible', 'Very flexible, plan me the best trip possible',),
    #
    # )
    STAGE = (
        ("I need more information before I can start trip planning",
         "I need more information before I can start trip planning",),
        ("I'm ready to start trip planning", "I'm ready to start trip planning",),
        ("I've done my homework and almost ready to book",
         "I've done my homework and almost ready to book",),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contacted = models.BooleanField(default=False)
    people = models.CharField(max_length=64, choices=PEOPLE_CHOICES, default='Couple')
    number_of_children = models.IntegerField(default=0)
    number_of_adults = models.IntegerField(default=0)
    country = models.CharField(max_length=255)
    bookedfor = models.DateField(blank=True,null=True)
    age_group = models.CharField(max_length=64, choices=AGE_GROUP, default='18-35 yrs')
    tour_type = models.CharField(max_length=100, choices=TOUR_TYPE, default='Group Tour')
    accomodation = models.CharField(max_length=100, choices=ACCOMODATIONS, default='Quirky')
    budget = models.FloatField(blank=True)
    # budget_flexibility = models.CharField(max_length=255, choices=FLEXIBILITY, default='Flexible,I can increase up to 20%,if needed')
    trip_stage = models.CharField(max_length=255, choices=STAGE, default="I'm ready to start trip planning")
    # trip_title = models.CharField(max_length=255,blank=True)
    # description = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('created_at',)