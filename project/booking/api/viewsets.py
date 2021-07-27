from rest_framework import viewsets
from project.booking.models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    model = Customer
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()