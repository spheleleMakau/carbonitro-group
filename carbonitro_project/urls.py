"""carbonitro_project URL Configuration."""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("", include("sitepages.urls")),
    path("companies/", RedirectView.as_view(url="/", permanent=False)),
    path("projects/", include("projects.urls")),
]
