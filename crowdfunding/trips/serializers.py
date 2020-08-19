from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    itinerary = serializers.CharField(max_length=1000)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    organiser = serializers.CharField(max_length=200)
    cost = serializers.IntegerField()
    duration = serializers.IntegerField()
    start_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Trip.objects.create(**validated_data)
