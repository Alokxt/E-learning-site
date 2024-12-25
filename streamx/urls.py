from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashvideos/',views.dashboard,name="dash-videos"),
]
