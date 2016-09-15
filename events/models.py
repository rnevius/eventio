from django.db import models

# Create your models here.
class Event(models.Model):
    capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField()
    # image = models.ImageField()
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.name
