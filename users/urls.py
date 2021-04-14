from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.users, name='users'),
    path('create/', views.users_create, name='users_create'),
    path('remove/', views.users_remove, name='users_remove'),
]