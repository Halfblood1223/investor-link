from django.shortcuts import render, HttpResponse

def deals(request):
    return render(request, 'deals/deals.html')

def deals_create(request):
    return render(request, 'deals/deals_create.html')

def deals_update(request):
    return render(request, 'deals/deals_update.html')

def deals_detail(request):
    return render(request, 'deals/deals_detail.html')