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


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["issue_description", "imei", "booking_date"]
