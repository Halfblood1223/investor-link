from django.shortcuts import render, HttpResponse

def plans(request):
    return render(request, 'plans/plans.html')