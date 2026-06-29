from django.urls import path
from . import views

urlpatterns = [
    path("", views.GenericPageView.as_view(), name="generic_page"),
]
