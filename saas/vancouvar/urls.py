from django.contrib import admin
from django.urls import path, include
from plans.models import EmailStats
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('account/', include('account.urls')),
    path('plans/', include('plans.urls'))
]

try:
    if len(EmailStats.objects.all()) < 1:
        email_stats = EmailStats.objects.create()
        email_stats.save()
except:
    print("Failed")
    pass