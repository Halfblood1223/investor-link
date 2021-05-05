from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from .forms import SignUpForm, UpdateForm, SignInForm, PassForgotForm, PassResetForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def account(request):
    if request.method == "POST":
        #creating form from inputs
        form = SignInForm(request.POST)
        if form.is_valid(): #checking form validity
            #trying to authenticate using given credentials
            user = authenticate(username=form.cleaned_data.get('email'), password=form.cleaned_data.get('cpassword'))
            if user != None: #if credentials are valid
                login(request, user) #logs in validated user
                return redirect('dashboard')
            else: #if credentials are invalid
                return redirect('account')
        else: #if form inputs are invalid
            return redirect('account')
    return render(request, 'account/account.html')

def account_create(request):
    if request.method == "POST":
        #turn the POST data into a form
        form = SignUpForm(request.POST)
        if form.is_valid():
            #if the inputs are valid then create a user with these credentials
            try:
                user = CustomUser.objects.create_user(email=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'), account_type=form.cleaned_data.get('account_type'))
            except:
                return redirect('account')
            user.save()
            login(request, user)
            return redirect('account_update')
        else:
            #if the inputs are invalid then redo the step
            return redirect('account_create')
    return render(request, 'account/account_create.html')


@login_required(login_url="/account")
def account_update(request):
    if request.method == "POST":
        #creating form of inputs
        form = UpdateForm(request.POST)
        if form.is_valid(): #checks form validity
            #if valid gets current user
            user = request.user
            if user != None: #if the user exists
                #fills out the new user updates
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.business_name = form.cleaned_data.get('business_name')
                user.business_website = form.cleaned_data.get('business_website')
                user.email_address = form.cleaned_data.get('email_address')
                user.problem_discovered = form.cleaned_data.get('problem_discovered')
                user.solution_proposed = form.cleaned_data.get('solution_proposed')
                user.founder_count = form.cleaned_data.get('founder_count')
                user.founder_background = form.cleaned_data.get('founder_background')
                user.competitive_advantage = form.cleaned_data.get('competitive_advantage')
                user.technology_stack = form.cleaned_data.get('technology_stack')
                user.current_stage = form.cleaned_data.get('current_stage')
                user.investor_return = form.cleaned_data.get('investor_return')
                user.incorporated_country = form.cleaned_data.get('incorporated_country')
                user.incorporated_state = form.cleaned_data.get('incorporated_state')
                user.adoption_strategy = form.cleaned_data.get('adoption_strategy')
                user.exit_strategy = form.cleaned_data.get('exit_strategy')
                user.target_market = form.cleaned_data.get('target_market')
                user.current_customers = form.cleaned_data.get('current_customers')
                user.retention_rate = form.cleaned_data.get('retention_rate')
                user.conversion_rate = form.cleaned_data.get('conversion_rate')
                user.product_availability = form.cleaned_data.get('product_availability')
                
                user.save()
                return redirect('dashboard') #once all info has been delivered they are sent to dashboard
            else: #if the user doesn't exist
                return redirect('account_create')
        else: #restarts process if form is invalid
            print("Invalid")
            return redirect("account_update")
    return render(request, 'account/account_update.html')

def log_out(request):
    logout(request)
    return redirect('https://en.vancouvar.com')