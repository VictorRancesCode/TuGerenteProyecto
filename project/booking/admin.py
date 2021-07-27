from django.contrib import admin
from .models import Customer, Room, Booking


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = "first_name", "last_name", "bo_ci", "bo_nit"
    list_display = "first_name", "last_name", "bo_ci", "bo_nit", "created_at"
    fieldsets = (
        ("", {
            "fields": ("first_name", "last_name",)
        }),
        ("Bolivia", {
            "fields": ("bo_ci", "bo_nit",)
        })
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = "name", "price", "created_at"
    search_fields = ["name"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    search_fields = "room__name",  "customer__bo_ci", "customer__bo_nit"
    list_filter = "status", "room", "check_in", "check_out"
    list_display = "room", "customer", "created_at", "check_in", "check_out"
    date_hierarchy = "created_at"
    readonly_fields = "status",
    autocomplete_fields = "room", "customer"

    def get_exclude(self, request, obj=None):
        if obj is None:
            return ["status", "payment_type", "paid_amount"]
        return super().get_exclude(request, obj)
    
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == Booking.State.PAID:
            return [*self.readonly_fields, "payment_type", "paid_amount"]

        return super().get_readonly_fields(request, obj=None)
