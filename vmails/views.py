from django.shortcuts import render, HttpResponse

def vmails(request):
    return render(request, 'vmails/vmails.html')