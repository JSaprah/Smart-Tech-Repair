from django import forms
from .models import Ticket, Phonemodel
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "phonemodel",
            "broken_part",
            "issue_description",
            "imei"
            ]
        widgets = {
            'issue_description': SummernoteWidget(),
            }

        phonemodel = forms.ModelChoiceField(
            queryset=Phonemodel.objects.all(),
            widget=forms.Select(),
            required=False
        )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
            )
