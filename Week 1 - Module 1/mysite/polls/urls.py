from django.urls import path

from . import views

urlpatterns = [
    path("", views.owner, name="home"),
    path("owner/", views.owner, name="owner"),
]