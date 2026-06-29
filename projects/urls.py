from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectsListView.as_view(), name="projects_list"),
]
