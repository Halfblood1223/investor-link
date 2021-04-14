from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [
    path('', views.account, name='account'),
    path('create/', views.account_create, name='account_create'),
    path('access/', views.account_access, name='account_access'),
    path('reset/', views.account_reset, name='account_reset'),
    path('settings/', views.account_settings, name='account_settings'),
]