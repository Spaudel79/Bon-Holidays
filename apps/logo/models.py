from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Logo(models.Model):
    image = models.ImageField(blank=True, null=True)
    # thumbnail = ImageSpecField(source='image',
    #                            processors=[ResizeToFill(100, 50)],
    #                            format='JPEG',
    #                            options={'quality': 60})
    # video = models.FileField(upload_to='', blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
