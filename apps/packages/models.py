from django.db import models

# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=255)
    duration = models.IntegerField(null=True)
    no_of_persons = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.destination}:{self.duration}:{self.price}"
