from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include("project.api.urls")),
    path('admin/', admin.site.urls),
]
