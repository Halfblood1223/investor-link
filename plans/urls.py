from django.contrib import admin
from django.urls import path, include
from plans import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.plans, name='plans'),
    path('angel', views.angelplan, name='angelplan'),
    path('venture', views.ventureplan, name='ventureplan'),
    path('office', views.officeplan, name='officeplan'),
    path('stripehook', csrf_exempt(views.stripehook), name='stripehook')
]