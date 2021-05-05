from django import forms

class PassForgotForm(forms.Form):
    email = forms.EmailField()

class PassResetForm(forms.Form):
    vcode = forms.IntegerField()
    password = forms.CharField()

class SignInForm(forms.Form):
    email = forms.EmailField()
    cpassword = forms.CharField()

class SignUpForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    account_type = forms.CharField()
    password = forms.CharField()
    cpassword = forms.CharField()

    def clean(self):
        super(SignUpForm, self).clean()

        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')

        if password != cpassword: #check if the two passwords match
            raise forms.ValidationError("Passwords do not match")

        return self.cleaned_data

class UpdateForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    business_name = forms.CharField(max_length=50)
    business_website = forms.URLField()
    email_address = forms.EmailField()
    problem_discovered = forms.CharField(max_length=50)
    solution_proposed = forms.CharField(max_length=50)
    founder_count = forms.CharField(max_length=50)
    founder_background = forms.CharField(max_length=50)
    competitive_advantage = forms.CharField(max_length=50)
    technology_stack = forms.CharField(max_length=50)
    current_stage = forms.CharField(max_length=50)
    investor_return = forms.CharField(max_length=50)
    incorporated_country = forms.CharField(max_length=50)
    incorporated_state = forms.CharField(max_length=50)
    adoption_strategy = forms.CharField(max_length=50)
    exit_strategy = forms.CharField(max_length=50)
    target_market = forms.CharField(max_length=50)
    current_customers = forms.CharField(max_length=50)
    retention_rate = forms.CharField(max_length=50)
    conversion_rate = forms.CharField(max_length=50)
    product_availability = forms.CharField(max_length=50)
    business_industry = forms.CharField(max_length=50)
    northstar_metric = forms.CharField(max_length=50)
    estimated_tam = forms.CharField(max_length=50)
    monthly_revenue = forms.CharField(max_length=50)
    current_arpu = forms.CharField(max_length=50)
    customer_ltv = forms.CharField(max_length=50)
    current_cac = forms.CharField(max_length=50)
    gross_margin = forms.CharField(max_length=50)
    magic_number = forms.CharField(max_length=50)
    current_valuation = forms.CharField(max_length=50)
    core_proceed = forms.CharField(max_length=50)
    raised_round = forms.CharField(max_length=50)
    current_round = forms.CharField(max_length=50)