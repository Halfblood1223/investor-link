from django.shortcuts import render, HttpResponse
from account.views import CustomUser
from django.http import JsonResponse
from django.conf import settings

from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import stripe

def plans(request):
    user = request.user
    ctx = {"user" : user}
    print(user.email_plan)
    return render(request, 'plans/plans.html', ctx)

def angelplan(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(success_url="http://127.0.0.1:8000", 
    cancel_url="http://127.0.0.1:8000/plans",
    payment_method_types=["card"], 
    line_items = [{"price" : "price_1InKLuDIUASXHMisRzxAQYEf", "quantity" : 1},],
    mode="subscription",)

    return JsonResponse({"id" : session.id})

def ventureplan(request):
    stripe.api_key =settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(success_url="http://127.0.0.1:8000", 
    cancel_url="http://127.0.0.1:8000/plans",
    payment_method_types=["card"], 
    line_items = [{"price" : "price_1InKMPDIUASXHMishEp3kAyb", "quantity" : 1},],
    mode="subscription",)

    return JsonResponse({"id" : session.id})

def officeplan(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(success_url="http://127.0.0.1:8000", 
    cancel_url="http://127.0.0.1:8000/plans",
    payment_method_types=["card"], 
    line_items = [{"price" : "price_1InKMxDIUASXHMissXzitZ58", "quantity" : 1},],
    mode="subscription",)

    return JsonResponse({"id" : session.id})

def stripehook(request):
    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_j2Luk6k962uwEVDKp7gz71XMV5QDOnOz'


    stripe.api_key = "sk_test_51Imb9WDIUASXHMiseg4asCebe7bE24gd0wrUx3VJgUo8Kt7a5rSFBagTa3mQ9kuSzMTfY3nDdDehg6DH998zml2l00Z3k176z0"

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the creation of a new subscription
    if event['type'] == 'customer.subscription.created':
        print(f"Customer ID: {event['data']['object']['customer']}")
        print(f"Product ID: {event['data']['object']['items']['data'][0]['plan']['product']} ") 

        customer = stripe.Customer.retrieve(event['data']['object']['customer'])  
        product = stripe.Product.retrieve(event['data']['object']['items']['data'][0]['plan']['product'])

        print(product)
        for user in CustomUser.objects.filter(email=customer["email"]).all():
            user.email_plan = product["name"]

            if product["name"] == "Venture":
                user.monthly_email_allowance = 40
                user.email_balance = 40
            elif product["name"] == "Office":
                user.monthly_email_allowance = 80
                user.email_balance = 80
            elif product["name"] == "Angel":
                user.monthly_email_allowance = 20
                user.email_balance = 20
            else:
                return HttpResponse(status=200)
            user.save()

    return HttpResponse(status=200)