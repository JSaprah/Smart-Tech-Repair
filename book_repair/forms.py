from django import forms
from .models import Customer, Service, Ticket


class PartForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['part']

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
        fields = ["issue_description", "imei"]
