from rest_framework import serializers
from .models import Trip, Pledge

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    trip_mate = serializers.CharField(max_length=200)
    trip_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

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

class TripDetailSerializer(TripSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)



    
