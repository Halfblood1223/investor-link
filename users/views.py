from django.shortcuts import render, HttpResponse

def users(request):
    return render(request, 'users/users.html')

def users_create(request):
    return render(request, 'users/users_create.html')

def users_remove(request):
    return render(request, 'users/users_remove.html')