from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    account_type = models.CharField(max_length=50)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    business_website = models.URLField()
    email_address = models.EmailField()
    problem_discovered = models.CharField(max_length=50, default="Agriculture")
    solution_proposed = models.CharField(max_length=50, default="5G")
    founder_count = models.CharField(max_length=50, default="~2")
    founder_background = models.CharField(max_length=50, default="Agriculture")
    competitive_advantage = models.CharField(max_length=50, default="Cheaper & Easier")
    technology_stack = models.CharField(max_length=50, default="5G")
    current_stage = models.CharField(max_length=50, default="Bootstrap")
    investor_return = models.CharField(max_length=50, default="~10%")
    incorporated_country = models.CharField(max_length=50, default="Canada")
    incorporated_state = models.CharField(max_length=50, default="Alberta")
    adoption_strategy = models.CharField(max_length=50, default="Affiliate Marketing")
    exit_strategy = models.CharField(max_length=50, default="IPO")
    target_market = models.CharField(max_length=50, default="B2B")
    current_customers = models.CharField(max_length=50, default="~000")
    retention_rate = models.CharField(max_length=50, default="~00%")
    conversion_rate = models.CharField(max_length=50, default="~00%")
    product_availability = models.CharField(max_length=50, default="Countywide")
    business_industry = models.CharField(max_length=50, default="Agriculture")
    northstar_metric = models.CharField(max_length=50, default="Daily Messages")
    estimated_tam = models.CharField(max_length=50, default="~$000M")
    monthly_revenue = models.CharField(max_length=50, default="~$00K")
    current_arpu = models.CharField(max_length=50, default="~$00")
    customer_ltv = models.CharField(max_length=50, default="~$000")
    current_cac = models.CharField(max_length=50, default="~$05")
    gross_margin = models.CharField(max_length=50, default="~00%")
    magic_number = models.CharField(max_length=50, default="~$0M")
    current_valuation = models.CharField(max_length=50, default="~$0M")
    core_proceed = models.CharField(max_length=50, default="R&D")
    raised_round = models.CharField(max_length=50, default="~$00K")
    current_round = models.CharField(max_length=50, default="~$000K")
    
    monthly_email_allowance = models.IntegerField(default=2)
    monthly_emails_sent = models.IntegerField(default=0)
    daily_emails_sent = models.IntegerField(default=0)
    weekly_emails_sent = models.IntegerField(default=0)
    email_balance = models.IntegerField(default=2)
    all_time_emails_sent = models.IntegerField(default=0)
    email_plan = models.CharField(default="CURIOUS", max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email