from rest_framework import viewsets
from project.booking.models import Customer, Room, Booking
from .serializers import CustomerSerializer, RoomSerializer, BookingSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    model = Customer
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()

class RoomViewSet(viewsets.ModelViewSet):
    model = Room
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all()
    
    

class BookingViewSet(viewsets.ModelViewSet):
    model = Booking
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.all()

