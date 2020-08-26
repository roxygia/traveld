from rest_framework import serializers
from .models import Trip, Pledge

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    trip_mate = serializers.ReadOnlyField(source='trip_mate.id')
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
    organiser = serializers.ReadOnlyField(source='organiser.id')
    cost = serializers.IntegerField()
    duration = serializers.IntegerField()
    start_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Trip.objects.create(**validated_data)

class TripDetailSerializer(TripSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.itinerary = validated_data.get('itinerary', instance.itinerary)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.organiser = validated_data.get('organiser', instance.organiser)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance




    
