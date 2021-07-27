from rest_framework import serializers
from project.booking.models import Customer, Room, Booking


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  "id", "first_name", "last_name", "bo_nit", "bo_ci"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields =  "id", "name", "price", "created_at", "updated_at"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields =  "id", "customer", "room", "status", "check_in", "check_out", "payment_type" ,"paid_amount", "created_at", "updated_at"
        read_only_fields = "status", "payment_type", "paid_amount", "updated_at"

class BookingPaySerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)
    payment_type = serializers.ChoiceField(choices=Booking.PaymentType, required=True)

class BookingCancelledSerializer(serializers.Serializer):
    security = serializers.BooleanField(default=False)