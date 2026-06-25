"""carbonitro_project URL Configuration."""
from django.urls import path, include

urlpatterns = [
    path("", include("sitepages.urls")),
]
