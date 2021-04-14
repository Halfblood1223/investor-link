from django.contrib import admin
from django.urls import path, include
from vmails import views

urlpatterns = [
    path('', views.vmails, name='vmails'),
]