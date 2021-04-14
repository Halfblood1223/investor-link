from django.contrib import admin
from django.urls import path, include
from deals import views

urlpatterns = [
    path('', views.deals, name='deals'),
    path('create/', views.deals_create, name='deals_create'),
    path('update/', views.deals_update, name='deals_update'),
    path('detail/', views.deals_detail, name='deals_detail'),
]