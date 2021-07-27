from rest_framework import serializers
from project.booking.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  "id", "first_name", "last_name", "bo_nit", "bo_ci"