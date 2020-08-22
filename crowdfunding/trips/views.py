from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trip, Pledge
from .serializers import TripSerializer, PledgeSerializer, TripDetailSerializer
from .permissions import IsOwnerOrReadOnly

class TripList(APIView):
    
    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organiser=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class TripDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        trip = self.get_object(pk)
        serializer = TripDetailSerializer(trip)
        return Response(serializer.data)

    def put(self, request, pk):
        trip = self.get_object(pk)
        data = request.data
        serializer = TripDetailSerializer(
            instance=trip,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()


class PledgeList(APIView):
    
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class PledgeDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Pledge.objects.get(pk=pk)
        except Pledge.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        trip = self.get_object(pk)
        serializer = PledgeSerializer(trip)
        return Response(serializer.data)


