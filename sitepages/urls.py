from django.urls import path
from . import views

urlpatterns = [
    path("", views.page_view, name="home"),
    path("about/", views.page_view, name="about"),
    path("services/", views.page_view, name="services"),
    path("contact/", views.page_view, name="contact"),
]
