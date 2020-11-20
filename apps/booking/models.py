from django.db import models
from apps.accounts.models import UserProfile, User
from apps.packages.models import Package
from ckeditor.fields import RichTextField

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package')
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