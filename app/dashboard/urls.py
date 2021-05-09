from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('user_create_admin', views.user_create_admin, name='user_create_admin'),
    path('emails_sent', views.emails_sent, name='emails_sent'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('<slug:slug>', views.unique_url, name="unique_url")
]