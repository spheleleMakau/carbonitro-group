from django.urls import path
from . import views

urlpatterns = [
    path("", views.CompaniesListView.as_view(), name="companies_list"),
    path("potific/", views.PotificDetailView.as_view(), name="company_potific"),
]
