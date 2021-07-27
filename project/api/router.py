from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Tu Gerente / Bookings API",
      default_version='v1',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="Victor"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

class Router(routers.DefaultRouter):
    include_format_suffixes = True
    include_root_view = False
