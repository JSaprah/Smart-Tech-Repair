from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = [
            "email",
            "broken_part",
            "issue_description",
            "imei"
            ]
        widgets = {
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter your email address", "class": "form-control"}),
            "broken_part": forms.Select(
                attrs={"class": "form-control"}),
            "issue_description": forms.Textarea(
                attrs={"placeholder": "Enter the description here", "class": "form-control"}),
        }


class EditTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = [
            "phonemodel",
            "email",
            "broken_part",
            "issue_description",
            "imei"
            ]

        widgets = {
            "phonemodel": forms.Select(
                attrs={"class": "form-control"}),
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter your email address", "class": "form-control"}),
            "broken_part": forms.Select(
                attrs={"class": "form-control"}),
            "issue_description": forms.Textarea(
                attrs={"placeholder": "Enter the description here", "class": "form-control"}),
        }



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
