from django import forms
from .models import Customer, Ticket


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "customer",
            "phonemodel",
            "broken_part",
            "issue_description",
            "imei"
            ]

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(), empty_label="Select a customer"
        )
