from django.shortcuts import render, HttpResponse

def account(request):
    return render(request, 'account/account.html')

def account_create(request):
    return render(request, 'account/account_create.html')

def account_access(request):
    return render(request, 'account/account_access.html')

def account_reset(request):
    return render(request, 'account/account_reset.html')

def account_settings(request):
    return render(request, 'account/account_settings.html')