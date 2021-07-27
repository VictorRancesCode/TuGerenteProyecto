from .router import Router, schema_view
from django.urls import re_path as url
from project.booking.api.viewsets import CustomerViewSet, RoomViewSet,BookingViewSet

router = Router()

router.register("customers", CustomerViewSet, basename="customer")
router.register("rooms", RoomViewSet, basename="room")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   *router.urls
]
