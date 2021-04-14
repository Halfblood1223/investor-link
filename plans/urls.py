from django.contrib import admin
from django.urls import path, include
from plans import views

urlpatterns = [
    path('', views.plans, name='plans'),
]