from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = [
            "broken_part",
            "issue_description",
            "imei"
            ]


class EditTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = [
            "phonemodel",
            "broken_part",
            "issue_description",
            "imei"
            ]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Password",
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirm Password",
        required=True,
    )

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
