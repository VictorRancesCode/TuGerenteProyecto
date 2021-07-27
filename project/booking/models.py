from django.db import models
from django.db.models import Q
from datetime import datetime 
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bo_nit = models.CharField(max_length=20, verbose_name="NIT", blank=True)
    bo_ci = models.CharField(max_length=20, verbose_name="CI", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RoomQuerySet(models.QuerySet):
    def available_now(self):
        return self.available_at(datetime.now())
    
    def available_date(self, date: datetime):
        return self.available_at(date)
    
    def available_at(self, checkin: datetime, checkout: datetime=None):
        if checkout:
            assert checkin < checkout, "Invalid range"
        else:
            checkout = checkin

        paid_bookings = (
            Booking.objects
            .filter(status=Booking.State.PAID)
            .filter(Q(check_in__gte=checkin) | Q(check_out__lte=checkout))
        )

        return self.exclude(bookings__in=paid_bookings)


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    # TODO: Deberia usar multiples monedas? django-money?
    price = models.IntegerField(null=True, help_text="Dia")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RoomQuerySet.as_manager()

    # Room.objects.all().available_now()
    # Room.objects.all().available_at()

    def __str__(self):
        return self.name


class Booking(models.Model):
    class State(models.TextChoices):
        PENDING = "pending", _("Pending")
        PAID = "paid", _("Paid")
        CANCELED = "canceled", _("Canceled")

    class PaymentType(models.TextChoices):
        CASH = "cash", _("Cash")
        CREDIT_CARD = "cc", _("Credit Card")
        BANK_DEPOSIT = "bank", _("Bank Deposit")

    customer = models.ForeignKey(Customer, related_name="bookings", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=State.choices, default=State.PENDING)
    
    # TODO: Si usuaremos DateTime deberia aplicar los conceptos de calculo mas complejos de hoteleria
    # REFERENCE: https://www.pearson.com/store/p/check-in-check-out-pearson-new-international-edition-managing-hotel-operations/P100000056832/9781292034355

    check_in = models.DateField()
    check_out = models.DateField()

    # TODO: Un mejor diseño seria un Modelo aparte, por hacerlo simple solo sera una columna
    payment_type = models.CharField(max_length=5, choices=PaymentType.choices, blank=True, null=True)
    paid_amount = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} {self.status}"

    def clean(self):
        # TODO: Validar fechas de checkin y checkout
        # TODO: Evitar rangos invalidos
        # TODO: Evitar completar bookings en fechas con conflicto
        pass

    def save(self, **kwargs):
        if self.id:
            if self.status == Booking.State.PENDING:
                if self.paid_amount == self.room.price:
                    self.status = Booking.State.PAID
        super().save(**kwargs)