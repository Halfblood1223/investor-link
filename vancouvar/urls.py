from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('account/', include('account.urls')),
    path('users/', include('users.urls')),
    path('plans/', include('plans.urls')),
    path('deals/', include('deals.urls')),
]