from rest_framework import viewsets
from project.booking.models import Customer, Room, Booking
from .serializers import CustomerSerializer, RoomSerializer, BookingSerializer, BookingPaySerializer, BookingCancelledSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


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

    @action(methods=['get'], detail=False, serializer_class=RoomSerializer)
    def available(self, request, **kwargs):
        try: 
            bookings = self.get_queryset().available_now()
            serializer = self.get_serializer(bookings, many=True)
            return Response(serializer.data,status= 200)
        except:
            return Response({'message':'Aplication Error'}, status =400)

class BookingViewSet(viewsets.ModelViewSet):
    model = Booking
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.all()

    @action(methods=['post'], detail=True, serializer_class=BookingPaySerializer)
    def pay(self, request, **kwargs):
        try: 
            amount = request.data['amount']
            payment_type = request.data['payment_type']
            booking = self.get_object()
            booking.paid_amount = amount
            booking.payment_type = payment_type
            booking.save()
            return Response(BookingSerializer(booking).data ,status = 200)
        except:
            return Response({'message':'Aplication Error'}, status =400)
    
    @action(methods=['post'], detail=True, serializer_class=BookingCancelledSerializer)
    def canceled(self, request, **kwargs):
        try: 
            security = request.data['security']
            booking = self.get_object()
            if booking.status == Booking.State.PENDING and security:
                booking.status = Booking.State.CANCELED
            return Response(BookingSerializer(booking).data ,status = 200)
        except:
            return Response({'message':'Aplication Error'}, status =400)