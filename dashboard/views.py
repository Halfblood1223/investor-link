from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from account.models import CustomUser
from account.views import account

from plans.models import EmailStats

from django.http import HttpResponseRedirect
from django.urls import reverse

import random
import os
import datetime as dt

def unique_url(request, slug):
    return redirect('account_create')

@login_required()
def admin_panel(request):
    user = request.user
    if not user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    for stat in EmailStats.objects.all():
        email_stats = stat

    ctx = {"email_stats" : email_stats}
    return render(request, 'dashboard/admin-panel.html', ctx)

@login_required(login_url='/account')
def dashboard(request):
    user = request.user
    acct = user.account_type
    if acct == "Investor":
        # recommend Founders/Business's
        # first look for overall best deals
        deals = []
        for founder in CustomUser.objects.filter(account_type="Founder").all(): #filter out investors
            currdata = vars(founder) #get the founder data
            compatability = 0 # how compatible they are
            for val in currdata: # check if values match
                currfval = currdata[val]
                currIval = getattr(user, val)
                if currfval == currIval:# if match add 3 to compatibility
                    compatability += 3
            if compatability >= 45: # if more than 45 compatible score then add to deals
                deals.append(founder)
            if len(deals) == 3: # gets the first 3 deals and leaves
                break
        # repeats the process for local users
        localdeals = []
        for founder in CustomUser.objects.filter(account_type="Founder", incorporated_state=user.incorporated_state).all():
            currdata = vars(founder)
            compatability = 0
            for val in currdata:
                currfval = currdata[val]
                currIval = getattr(user, val)
                if currfval == currIval:
                    compatability += 3
            if compatability >= 45:
                localdeals.append(founder)
            if len(localdeals) == 3:
                break
        #repeats the process for industry users
        industrydeals = []
        for founder in CustomUser.objects.filter(account_type="Founder", business_industry=user.business_industry).all():
            currdata = vars(founder)
            compatability = 0
            for val in currdata:
                currfval = currdata[val]
                currIval = getattr(user, val)
                if currfval == currIval:
                    compatability += 3
            if compatability >= 45:
                industrydeals.append(founder)
            if len(industrydeals) == 3:
                break
        # passes the deals as context to the html template
        ctx = {"username" : user.first_name}
        for x in range(3):
            try:
                ctx["user" + str(x + 1)] = deals[x]
                ctx[f"user{x+1}_string"] = False
            except:
                ctx[f"user{x+1}_string"] = True
            try:
                ctx["localuser" + str(x + 1)] = localdeals[x]
                ctx[f"localuser{x+1}_string"] = False
            except:
                ctx[f"localuser{x+1}_string"] = True
            try:
                ctx["industryuser" + str(x + 1)] = industrydeals[x]
                ctx[f"industryuser{x+1}_string"] = False
            except:
                ctx[f"industryuser{x+1}_string"] = True

        print(ctx)
        return render(request, 'dashboard/dashboard.html', ctx)
    elif acct == "Founder":
        # recommend Investors
        # first look for overall best deals
        deals = []
        for investor in CustomUser.objects.filter(account_type="Investor").all(): #filter out founders
            currdata = vars(investor) #get the investor data
            compatability = 0 # how compatible they are
            for val in currdata: # check if values match
                currIval = currdata[val]
                currfval = getattr(user, val)
                if currfval == currIval:# if match add 3 to compatibility
                    compatability += 3
            if compatability >= 45: # if more than 45 compatible score then add to deals
                deals.append(investor)
            if len(deals) == 3: # gets the first 3 deals and leaves
                break
        # repeats the process for local users
        localdeals = []
        for investor in CustomUser.objects.filter(account_type="Investor", incorporated_state=user.incorporated_state).all():
            currdata = vars(investor)
            compatability = 0
            for val in currdata:
                currIval = currdata[val]
                currfval = getattr(user, val)
                if currfval == currIval:
                    compatability += 3
            if compatability >= 45:
                localdeals.append(investor)
            if len(localdeals) == 3:
                break
        #repeats the process for industry users
        industrydeals = []
        for investor in CustomUser.objects.filter(account_type="Investor", business_industry=user.business_industry).all():
            currdata = vars(investor)
            compatability = 0
            for val in currdata:
                currIval = currdata[val]
                currfval = getattr(user, val)
                if currfval == currIval:
                    compatability += 3
            if compatability >= 45:
                industrydeals.append(investor)
            if len(industrydeals) == 3:
                break
        # passes the deals as context to the html template
                # passes the deals as context to the html template
        ctx = {"username" : user.first_name}
        for x in range(3):
            try:
                ctx["user" + str(x + 1)] = deals[x]
                ctx[f"user{x+1}_string"] = False
            except:
                ctx[f"user{x+1}_string"] = True
            try:
                ctx["localuser" + str(x + 1)] = localdeals[x]
                ctx[f"localuser{x+1}_string"] = False
            except:
                ctx[f"localuser{x+1}_string"] = True
            try:
                ctx["industryuser" + str(x + 1)] = industrydeals[x]
                ctx[f"industryuser{x+1}_string"] = False
            except:
                ctx[f"industryuser{x+1}_string"] = True
            
        print(ctx)
        return render(request, 'dashboard/dashboard.html', ctx)
    else:
        return redirect('account') #account type doesn't show up
    return render(request, 'dashboard/dashboard.html')




@login_required()
def user_create_admin(request):

        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'names.txt')   #full path to text.
        data_file = open(file_path , 'r')       
        name_list = [line for line in data_file.readlines()]

        problem_discovered_list = ["Agriculture", "Automotive", "Education", "Finance",
        "Hardware", "Healthcare", "Hospitality", "Retail", "Software", "Other"]

        solution_proposed_list = ["5G", "AI", "AR/VR", "Biometrics", "Blockchain", "Cloud", "DevOps"
        ,"Drone", "Quantum", "Robotics"]

        founder_count_list = ["~2", "~4", "~6", "~8"]

        founder_background_list = problem_discovered_list[:]

        competitive_advantage_list = ["Cheaper & Easier", "Cheaper & Faster", "Cheaper & Safer", "Easier & Faster"
        , "Easier & Safer", "Safer & Faster"]

        technology_stack_list = solution_proposed_list[:]

        current_stage_list = ["Bootstrap", "Pre Seed", "Seed", "Post Seed", "Series A", "Series B", "Series C"]

        investor_return_list = ["~10%", "~13%", "~15%", "~17%", "~19%"]

        incorporated_country_list = ["Canada", "United States"]

        incorporated_state_list = {"Canada" : ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador",
        "Nova Scotia", "Northwest Territories", "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", 
        "Yukon"], "United States" : ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
        "District Of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
        "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota","Mississippi","Missouri","Montana",
        "Nebraska", "Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota",
        "Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee",
        "Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]}
        

        adoption_strategy_list = ["Affiliate Marketing", "Channel Partnerships", "Content Marketing", "Display Advertising", "Email Marketing"
        ,"Network Effects","Referral Marketing","Reseller Programs","Search Advertising","Social Media Marketing"]

        exit_strategy_list = ["IPO", "Merger", "Acquisition"]

        target_market_list = ["B2B", "B2C", "B2G"]

        current_customers_list = ["~000", "~200", "~400","~600","~800"]

        retention_rate_list = ["~00%","~20%","~40%","~60%","~80%"]

        conversion_rate_list = ["~00%","~10%","~13%","~16%","~19%"]
        
        product_availability_list = ["Countywide","Citywide","Statewide","Nationwide","Worldwide"]

        business_industry_list = problem_discovered_list[:]

        northstar_metric_list = ["Daily Messages", "Daily Purchases", "Daily Users", "Monthly Messages"
        ,"Monthly Purchases", "Monthly Users", "Weekly Messages", "Weekly Purchases", "Weekly Users"]

        estimated_tam_list = ["~$000M","~$200M","~$400M","~$600M","~$800M"]

        monthly_revenue_list = ["~$00K", "~$20K", "~$40K", "~$60K", "~$80K"]

        current_arpu_list = ["~$00", "~$20", "~$40", "~$60", "~$80"]

        customer_ltv_list = ["~$000", "~$200", "~$400", "~$600", "~$800"]

        current_cac_list = ["~$05", "~$20", "~$40", "~$60", "~$80"]

        gross_margin_list = ["~00%", "~20%", "~40%", "~60%", "~80%"]

        magic_number_list = ["~0.5x", "~2.0x", "~4.0x", "~6.0x", "~8.0x"]

        current_valuation_list = ["~$0M", "~$2M", "~$4M", "~$6M", "~$8M"]

        core_proceed_list = ["R&D", "Hiring", "Adoption", "Operations", "Acquisition"]

        raised_round_list = ["~$00K", "~$20K", "~$40K", "~$60K", "~$80K"]

        current_round_list = ["~$000K", "~$200K", "~$400K", "~$600K", "~$800K"]


        
        for account_num in range(292): # creates founders with Random choices
            user = CustomUser.objects.create_user(email=name_list[account_num].split(" ")[0] + "@mailinator.com", password="Yashveer1", account_type="Founder")
            print(f'User number -> {account_num}')
            #filling in all the required fields for an account
            user.first_name = name_list[account_num].split(" ")[0]
            user.last_name = name_list[account_num].split(" ")[1]
            user.business_name = name_list[account_num] + " TEST BUSINESS"
            user.business_website = "google.com"
            user.email_address = name_list[account_num].split(" ")[0] + "@mailinator.com"
            user.problem_discovered = random.choice(problem_discovered_list)
            user.solution_proposed = random.choice(solution_proposed_list)
            user.founder_count = random.choice(founder_count_list)
            user.founder_background = random.choice(founder_background_list)
            user.competitive_advantage = random.choice(competitive_advantage_list)
            user.technology_stack = random.choice(technology_stack_list)
            user.current_stage = random.choice(current_stage_list)
            user.investor_return = random.choice(investor_return_list)
            country = random.choice(incorporated_country_list)
            user.incorporated_country = country
            user.incorporated_state = random.choice(incorporated_state_list[country])
            user.adoption_strategy = random.choice(adoption_strategy_list)
            user.exit_strategy = random.choice(exit_strategy_list)
            user.target_market = random.choice(target_market_list)
            user.current_customers = random.choice(current_customers_list)
            user.retention_rate = random.choice(retention_rate_list)
            user.conversion_rate = random.choice(conversion_rate_list)
            user.product_availability = random.choice(product_availability_list)
            user.business_industry = random.choice(business_industry_list)
            user.northstar_metric = random.choice(northstar_metric_list)
            user.estimated_tam = random.choice(estimated_tam_list)
            user.monthly_revenue = random.choice(monthly_revenue_list)
            user.current_arpu = random.choice(current_arpu_list)
            user.customer_ltv = random.choice(customer_ltv_list)
            user.current_cac = random.choice(current_cac_list)
            user.gross_margin = random.choice(gross_margin_list)
            user.magic_number = random.choice(magic_number_list)
            user.current_valuation = random.choice(current_valuation_list)
            user.core_proceed = random.choice(core_proceed_list)
            user.raised_round = random.choice(raised_round_list)
            user.current_round = random.choice(current_round_list)

            user.save() #saves user in the database

        return redirect('dashboard')

@user_passes_test(lambda u: u.is_superuser)
def emails_sent(request):
    curr_date = dt.datetime.today()

    