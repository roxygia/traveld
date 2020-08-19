from django.db import models

# Create your models here.

class Trip(models.Model):
    title = models.CharField(max_length=200)
    itinerary = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    organiser = models.CharField(max_length=200)
    cost = models.IntegerField()
    duration = models.IntegerField()
    start_date = models.DateTimeField()

