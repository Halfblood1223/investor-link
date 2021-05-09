from __future__ import absolute_import, unicode_literals

import os
import django

from celery import Celery
from celery.schedules import crontab

from django.core.mail import send_mail
from time import sleep

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vancouvar.settings')

django.setup()

from account.models import CustomUser

from plans.models import EmailStats

app = Celery('vancouvar')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(crontab(minute='0', hour='8'), daily_emails.s(), name='daily_emails')
    sender.add_periodic_task(crontab(hour=1, month="*"), monthly_reset.s(), name='monthly_reset')
    sender.add_periodic_task(crontab(hour=2, day="*"), daily_reset.s(), name="daily_reset")
    sender.add_periodic_task(crontab(hour=3, day="0"), weekly_reset.s(), name="weekly_reset")

@app.task()
def weekly_reset():
    for user in CustomUser.objects.all():
        user.weekly_emails_sent = 0
        user.save()
    for stat in EmailStats.objects.all():
        stat.weekly = 0
        stat.save()

@app.task()
def daily_reset(): # resets email limits & stats daily 
    for user in CustomUser.objects.all():
        user.daily_emails_sent = 0
        user.save()
    for stat in EmailStats.objects.all():
        stat.daily = 0
        stat.save()

@app.task()
def monthly_reset(): # resets emails limits once a month
    for user in CustomUser.objects.all():
        user.monthly_emails_sent = 0
        user.email_balance = user.monthly_email_allowance
        user.save()
    for stat in EmailStats.objects.all():
        stat.monthly = 0
        stat.save()
    print("Monthly Reset Completed")

@app.task()
def daily_emails(): # sends daily deals to users
    for stat in EmailStats.objects.all():
        emailstatcollecter = stat
    for user in CustomUser.objects.all(): # start looking for deals for all users
        if user.monthly_emails_sent < user.monthly_email_allowance: # check if email allowance is already exceeded before starting search | saves computation power
            deals = []
            for user2 in CustomUser.objects.all(): # searches through all users
                if user != user2: # checks if the users are the same:
                    currdata = vars(user2) # the values of the searched user
                    compatability = 0 #reset compatability value per user
                    for val in currdata:
                        curr2val = currdata[val] # retrieves specific values of searched user
                        curr1val = getattr(user, val) # retrieves specific values of the searching user
                        if curr2val == curr1val: # increases score by 3 if vals match
                            compatability += 3
                        if compatability >= 45: # if compatability is high enough then add to deals
                            deals.append(user2)
                            break
                    if len(deals) == 3: # if three deals have been compiled then stop looking for deals
                        break
                else:
                    print("Duplicate") # if user and user2 are the same people skip to next person
            # start the emailing execution
            for deal in deals: # cycle through all the compiled deals
                if user.monthly_emails_sent >= user.monthly_email_allowance: # if monthly email allowance exceeded stop sending emails
                    print(user.first_name.rstrip(), user.last_name.rstrip(), user.monthly_emails_sent, user.monthly_email_allowance)
                    break
                subject = f"Investment Deal for {user.first_name.rstrip()} {user.last_name.rstrip()} - Vancouvar"
                message = f"Hello {user.first_name.rstrip()}, \n I'd like to tell you about {deal.business_name.rstrip()}, a {deal.current_stage.rstrip()} startup in {deal.incorporated_state.rstrip()}, {deal.incorporated_country.rstrip()} with a {deal.magic_number.rstrip()} magic number and {deal.gross_margin.rstrip()} gross margin. \n We are in the {deal.business_industry.rstrip()} market, sit on {deal.monthly_revenue.rstrip()} monthly revenue and looking forward to raising {deal.current_round.rstrip()} at a {deal.current_valuation.rstrip()} valuation. \n Would you be interested in this? \n -- {deal.first_name.rstrip()} \n {deal.business_website.rstrip()}"
                send_mail(subject, message, 'Vancouvar Team <support@vancouvar.com>', [user.email], fail_silently=False)
                print(f"Message sent about {deal.business_name} to {user.first_name} {user.last_name}")
                user.monthly_emails_sent += 1
                user.daily_emails_sent += 1
                user.weekly_emails_sent += 1
                emailstatcollecter.monthly += 1
                emailstatcollecter.daily += 1
                emailstatcollecter.weekly += 1
                emailstatcollecter.all_time += 1
                user.save()
                sleep(10)
        else:
            print("Monthly Emails Exceeded")
    print("Daily Emails Sent")

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))