from django import forms
from django_countries.fields import CountryField


class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036 )]
    
    full_name = forms.CharField(label="Name")
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code(CVV)', required=False)
    expiry_year = forms.ChoiceField(label='year', choices=YEAR_CHOICES, required=False)
    expiry_month = forms.ChoiceField(label='month', choices=MONTH_CHOICES, required=False)
    country = CountryField().formfield()
    stripe_id = forms.CharField(widget=forms.HiddenInput)
