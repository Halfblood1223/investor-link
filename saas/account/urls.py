from django.contrib import admin
from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.account, name='account'),
    path('create/', views.account_create, name='account_create'),
    path('forgot/', auth_views.PasswordResetView.as_view(template_name='account/account_forgot.html'), name='password_reset'),
    path('reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(template_name='account/account_reset.html', success_url=reverse_lazy('dashboard')), name='password_reset_confirm'),
    path('update/', views.account_update, name='account_update'),
    path('forgot/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #need a template for this page
    path('logout', views.log_out, name='logout')
    #path('detail/', views.account_detail, name='account_detail'),
]