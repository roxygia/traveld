from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Trip(models.Model):
    title = models.CharField(max_length=200)
    itinerary = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    organiser = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='organiser_trips'
    )
    cost = models.IntegerField()
    duration = models.IntegerField()
    start_date = models.DateTimeField()

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    trip = models.ForeignKey(
        'Trip',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    trip_mate = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='trip_mate_pledges'
    )

